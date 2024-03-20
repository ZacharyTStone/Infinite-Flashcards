# AI-Language-Learning-Flashcards

This project is a Python script and soon to be web app that generates Anki cards from a word list using OpenAI. The generated cards include word readings, example sentences, and basic definitions.

(currently, only Japanese cards are supported. This will change in the future)

## Requirements

- Python 3
- OpenAI API key
- AnkiConnect (if automatically importing into Anki)

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your OpenAI API key in the `.env` file:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
3. Set your AnkiConnect key in the `.env` file (if automatically importing into Anki):

   - [AnkiConnect](https://ankiweb.net/shared/info/2055492159)

   ```
    ANKI_CONNECT_URL=your AnkiConnect local host address
   ```

4. run create_text_files.py to create the necessary text files for the card generations
   ```bash
   python create_text_files.py
   ```

## Usage

1. Add words to the words.txt file

2. Make sure the Anki app is open.

2. Run the main.py script:

   ```bash
   python main.py
   ```

2. follow the prompts. The script will generate the cards using the Open AI key, and the app will create the CSV files and import them into Anki automatically.

## Structure

- .env
- .gitignore
- README.md
- requirements.txt
- create_text_files.py
- main.py
- word-based-cards
  - generate_csv.py
  - make_anki_pkg.py
  - import_to_anki.py

## Notes

- Be sure to set your OpenAI API key in a `.env` file.
- If using AnkiConnect to automatically import cards into Anki update the ANKI_CONNECT_URL in the `.env` file to the local address of AnkiConnect.

## License

MIT
