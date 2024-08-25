import edge_tts
import asyncio
from pydub import AudioSegment
from playsound import playsound

# en-US-AndrewNeural : male
# en-US-AvaMultilingualNeural : female

def change_speed_and_pitch(file_path, output_path, speed_change=1.0):
    audio = AudioSegment.from_file(file_path)
    
    # Change speed
    new_sample_rate = int(audio.frame_rate * speed_change)
    audio = audio._spawn(audio.raw_data, overrides={'frame_rate': new_sample_rate})
    audio = audio.set_frame_rate(44100)
    
    # Save the file with changed speed of speech
    audio.export(output_path, format="mp3")

    



async def amain(TEXT,OUTPUT_FILE,VOICE="en-US-AvaMultilingualNeural",SPEED=1) -> None:
    """Main function"""
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)
    if(SPEED != 1):
        change_speed_and_pitch(OUTPUT_FILE,OUTPUT_FILE,speed_change=SPEED)
    playsound(OUTPUT_FILE)
        



if __name__=="__main__":
    text="The prime minister of India is Narendra Modi. He is a very humble person"
    filename="llm_voice_output/output.mp3"
    asyncio.run(amain(text,filename))
    change_speed_and_pitch(filename,"llm_voice_output/output_mod.mp3",speed_change=1)