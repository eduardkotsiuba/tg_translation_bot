# AI-Powered Telegram Translator

A Telegram bot that uses the OpenAI API to translate text between eight languages.

Users can choose a source and target language, swap the selected languages, or start the selection process again.

## Features

- Translation between English, German, Czech, Ukrainian, French, Spanish, Russian, and Dutch
- Language selection using Telegram buttons
- Option to swap the selected languages
- Option to restart the language selection

## Technologies

- Python
- aiogram
- OpenAI Python SDK
- python-dotenv

## Requirements

- Python
- A Telegram bot token from BotFather
- An OpenAI API key

## Setup

1. Download or clone the repository.
2. Open a terminal in the project folder.
3. Create a virtual environment:

   ```powershell
   python -m venv .venv
   ```

4. Activate the virtual environment:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

5. Install the required packages:

   ```powershell
   pip install -r requirements.txt
   ```

6. Create a file named `.env` in the project folder and add your credentials:

   ```text
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   OPENAI_API_KEY=your_openai_api_key
   ```

7. Start the bot:

   ```powershell
   python run.py
   ```

## Security

The `.env` file contains private credentials and must not be uploaded to GitHub. Never share your bot token or API key publicly.

## Demo

[Watch the project demo on YouTube](https://youtu.be/IxyJj462L0o)
