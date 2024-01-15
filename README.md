# ChatBot Quickstart

This is a minimalist starting point for a chat bot, written in Python. It uses the OpenAI API. Easily edit the system prompt to create a unique AI personality or function.

![Screenshot](https://github.com/ibra-kdbra/Robot-bot/blob/main/example.png)

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Clone this repository.

3. Navigate into the project directory:

   ```bash
   cd ROBOT-BOT
   ```

4. Create a new virtual environment:

   ```bash
   python3 -m venv venv
   . venv/bin/activate
   ```

5. Install the requirements:

   ```bash
   pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file:

   ```bash
   cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file.

8. Tell the AI how to behave by editing the file templates/system_prompt.txt.
9. Run the app:

   ```bash
   flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! To learn more, check out the [Open AI tutorial](https://beta.openai.com/docs/quickstart).
