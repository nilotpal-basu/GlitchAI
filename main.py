import requests
import time
import asyncio
from speech_to_text import transcribe
from text_to_speech import amain

def start_chat_client(voice,speed=1):
    # FastAPI server URL
    server_url = "your_public_ngrok_url/chat"  # Adjust URL if using ngrok

    while True:
        user_input=transcribe() # Your speech is converted into text

        print("Your input : " + user_input)

        if(user_input.lower().strip() == "exit."):
            break  # Exits from the loop and ends the program

        try:
            response = requests.post(server_url, json={"message": user_input})
            response.raise_for_status()  # Raise an error for bad responses

            # Get the server's response
            server_response = response.json().get("response", "No response from server")
            print("Server response:", server_response)

            # Appending the server responses to an output log file
            with open("output_log.txt","a+") as output_log:
                output_log.write(server_response+"\n")
                output_log.close()

            asyncio.run(amain(server_response,f"llm_voice_output/output.mp3",voice,speed))

        except requests.RequestException as e:
            print(f"An error occurred: {e}")

        
        time.sleep(2)

if __name__ == "__main__":

    # Initializing the gender of your Voice Assistant
    gender=str(input("Enter the gender of your voice assistant (male or female) : "))

    # Initializing the voice based on your given preference
    if(gender.lower().strip()[0] == 'm'):
        voice="en-US-AndrewNeural"
    else:
        voice="en-US-AvaMultilingualNeural"
    
    # Starting the conversation with the LLM
    start_chat_client(voice)
