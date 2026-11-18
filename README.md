# Gemini Chatbot & Prompt Engineering

A beginner-friendly Generative AI project built using Python and Google's Gemini API. This repository contains prompt engineering exercises, experiments with model parameters, and a conversational chatbot with a Streamlit web interface.

## Features

- Prompt engineering exercises, including clear instructions, structured output and text summarization
- Experiments with temperature, output token limits and context
- CLI chatbot with conversation history
- Clear conversation and exit commands in the CLI version
- Browser-based chat interface built with Streamlit
- Secure API key configuration using environment variables and Streamlit Secrets

## Tech Stack

- Python
- Google Gemini API (`google-genai`)
- Streamlit
- python-dotenv

## Project Structure

```text
genai-prompt-engineering/
├── day1.py
├── day2.py
├── day3_chatbot.py
├── chat_app.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/kavyachirumallaa-sys/genai-prompt-engineering.git
cd genai-prompt-engineering
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here
```

Get an API key from Google AI Studio. Never commit your `.env` file or share your API key.

### 5. Run the CLI chatbot

```bash
python day3_chatbot.py
```

### 6. Run the web app

```bash
python -m streamlit run chat_app.py
```

## Deployment

The Streamlit web app is deployed using Streamlit Community Cloud. The Gemini API key is configured through the app's Secrets settings rather than committed to the repository.

**Live Demo:*https://kavya-gemini-chatbot.streamlit.app/* Add your deployed Streamlit app URL here.

## What I Learned

- Writing clearer prompts for language models
- Understanding temperature and output token limits
- Managing conversation history in a chatbot
- Calling the Gemini API from Python
- Building a web interface with Streamlit
- Managing environment variables and deployment secrets
- Pushing code to GitHub and deploying a Python application

## Future Improvements

- Add conversation export and persistent chat history
- Improve API error handling and rate-limit management
- Add configurable model settings
- Improve the user interface and usability

## Author

Kavya

[GitHub Repository](https://github.com/kavyachirumallaa-sys/genai-prompt-engineering)
