import requests
import time
import asyncio
from speech import transcribe
from text_to_speech import amain

def start_chat_client(voice,speed=1):
    c=0
    # FastAPI server URL
    server_url = "your_public_ngrok_url/chat"  # Adjust URL if using ngrok

    while True:
        user_input=transcribe()
        print("Your input : " + user_input)
        if(user_input.lower().strip() == "exit."):
            break
        try:
            response = requests.post(server_url, json={"message": user_input})
            response.raise_for_status()  # Raise an error for bad responses

            # Get the server's response
            server_response = response.json().get("response", "No response from server")
            print("Server response:", server_response)

            with open("output_log.txt","a+") as output_log:
                output_log.write(server_response+"\n")
                output_log.close()

            asyncio.run(amain(server_response,f"llm_voice_output/output.mp3",voice,speed))
            c+=1

        except requests.RequestException as e:
            print(f"An error occurred: {e}")
        time.sleep(2)

if __name__ == "__main__":
    gender=str(input("Enter the gender of your voice assistant (male or female) : "))
    if(gender.lower().strip()[0] == 'm'):
        voice="en-US-AndrewNeural"
    else:
        voice="en-US-AvaMultilingualNeural"
    start_chat_client(voice)
