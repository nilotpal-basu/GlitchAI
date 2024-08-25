import torch
import tensorflow as tf
from transformers import pipeline
from transformers.pipelines.audio_utils import ffmpeg_microphone_live
import sys

# Choosing the device
device = "cuda:0" if torch.cuda.is_available() else "cpu"

transcriber = pipeline(
    "automatic-speech-recognition", model="openai/whisper-base.en", device=device
)
# Initialize the Whisper model
def transcribe(chunk_length_s=8, stream_chunk_s=1):

    mic = ffmpeg_microphone_live(
        sampling_rate=16000, # Sampling rate of 16KHz
        chunk_length_s=chunk_length_s, # Time for which the input will be taken
        stream_chunk_s=stream_chunk_s,
    )

    print("Start speaking...")
    for item in transcriber(mic, generate_kwargs={"max_new_tokens": 128}):
        sys.stdout.write("\033[K")
        print(item["text"], end="\r")
        if not item["partial"][0]:
            break

    # Appending the inputs from the mic into an input log file
    with open("input_log.txt","a+") as log_file:
        log_file.write(item["text"]+"\n")
        log_file.close()
    return item["text"]

if __name__ == "__main__":
    transcribe()