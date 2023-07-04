# Pablo AI

Pablo AI is a voice-based AI assistant that allows users to interact with an artificial intelligence model using voice commands. The assistant utilizes various technologies and APIs to perform tasks such as retrieving information, opening websites, and engaging in conversation.

## Features

- Voice Recognition: Pablo AI can understand voice commands from the user using the SpeechRecognition library.
- Information Retrieval: The assistant can fetch information from Wikipedia based on user queries.
- Natural Language Processing: The assistant uses the `pyttsx3` library to convert text into speech, enabling a conversational experience.
- Website Opening: Pablo AI can open websites based on user commands.
- Time Reporting: Users can ask the assistant for the current time, and it will provide the information.
- Conversational AI: The OpenAI GPT-3 model is used to engage in conversation and provide responses based on user queries.

## Installation

To run the Pablo AI project, follow these steps:

1. Clone or download the repository to your local machine.
2. Install the required dependencies by running the following command:
```shell
   pip install pyttsx3
   pip install SpeechRecognition
   pip install wikipedia-api
   pip install openai
4. Obtain the required API key for the OpenAI GPT-3 model.
5. Replace the placeholder API key in the `config.py` file with your actual API key.

## Usage

1. Run the Python script `pablo.py`.
2. Once the assistant is initialized, it will greet you and wait for your voice command.
3. Speak clearly and provide a voice command or ask a question.
4. The assistant will interpret the command and perform the appropriate action, such as opening a website or retrieving information.
5. For conversational queries, the assistant will use the OpenAI GPT-3 model to generate responses.
6. To stop the assistant, you can say "Pablo stop" or exit the program.
## Examples

Here are a few examples of how to interact with Pablo AI:

1. **Open Websites**: Say commands like "Open YouTube," "Open Wikipedia," or "Open Google" to see Pablo AI open the respective websites.
2. **General Knowledge**: Test the AI's knowledge with queries like "Who is the president of the United States?" or "When was the Eiffel Tower built?"

Feel free to explore and interact with the assistant using natural language commands.

## Contributing

Contributions to the Pablo AI project are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them: `git commit -m 'Add your commit message'`.
4. Push your changes to your forked repository: `git push origin feature/your-feature-name`.
5. Submit a pull request to the main branch of the original repository.

## License

This project is licensed under the MIT License. 
