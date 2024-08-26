
# GlitchAI

![glitchAI_img](https://github.com/user-attachments/assets/f8076ac9-4dc5-4838-874d-63325397bf70)


GlitchAI is a real-time speech-to-speech voice assistant designed to revolutionize your interactions with technology. With its advanced natural language processing capabilities and intuitive voice interface, GlitchAI understands your spoken requests and responds in a clear, human-like voice.



## Features

- Speech Recognition : Accurate and fast conversion of spoken words to text.
- Text-to-Speech: Natural and clear speech generation from text.
- Contextual Awareness: Understanding of conversation context for tailored responses.
- Entertainment: Storytelling, jokes, poetry, content - recommendations, trip planning.
- Productivity: Task management and reminders.

## Technologies

- Speech-to-Text: OpenAI's [Whisper](https://github.com/openai/whisper) base English model
- Language Model: [Gemini 1.5 Flash](https://github.com/matiassingers/awesome-readme) integrated with LangChain
- Local Deployment: Ngrok
- Text-to-Speech: [Edge-TTS](https://github.com/rany2/edge-tts)
- Programming Language: Python

## Installation and Usage
### Prerequisites:

- Python 3.10.x
- Required libraries (install using pip install -r requirements.txt)

### STEP 1: Clone the repository
```bash
git clone https://github.com/nilotpal-basu/GlitchAI.git
```
### STEP 2: Set up environment variables

 GOOGLE_GEMINI_KEY: Your Google Gemini API key

NGROK_AUTHTOKEN: Your Ngrok authtoken

### STEP 3: Setting up the LLM server in Google Colab
- Open Google Colab: Go to https://colab.google/.
- Upload the file: Upload the `llm_server.ipynb` file to Google Colab.
- Run the cells: Execute the cells in the notebook, following the instructions provided.
- Obtain Ngrok URL: The notebook will output the Ngrok URL once the tunnel is established.
- Copy that URL and paste it in `main.py` in place of `your_public_ngrok_url`.

### STEP 4: Run the application

```bash
python main.py
```
### STEP 5: Usage
Speak into your microphone to interact with GlicthAI.
The assistant will respond verbally and in text.

  
## Contributing
Contributions are welcome! Please follow these guidelines:
- Fork the repository.
- Create a new branch for your feature or bug fix.   
- Make your changes and commit them.
- Submit a pull request to the main branch.


## License

This project is licensed under the [MIT](https://github.com/nilotpal-basu/GlitchAI/blob/main/LICENSE) License. 

