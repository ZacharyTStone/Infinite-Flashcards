# Endless Flashcards

This project is a Python script that generates Japanese Anki flashcards from a word list using OpenAI. 

The generated cards include word readings, pitch accent, example sentences, and definitions.

This Python script significantly simplifies the process of creating new cards, allowing advanced learners to focus on studying rather than card creation.

The cards are 100% in Japanese so this is suitable for advanced users who can learn in Japanese. I may add a hiragana only option in the future.

## Requirements

- Python
- OpenAI API key
- Anki + AnkiConnect

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your OpenAI API key in the `.env` file:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
3. Set your AnkiConnect key in the `.env` file

   - [AnkiConnect Extention](https://ankiweb.net/shared/info/2055492159)

   ```
    ANKI_CONNECT_URL=your AnkiConnect local host address
   ```

4. Run the main.py script to create the words.txt file in the card_generation_scripts folder:

   ```bash
   python main.py
   ```

## Usage

1. Add words to the words.txt file

2. Make sure the Anki app is open.

3. Run the main.py script:

   ```bash
   python main.py
   ```

4. follow the prompts. The script will generate the cards using the Open AI key, and the app will create the CSV files and import them into Anki automatically.

## Structure

- .env
- .gitignore
- README.md
- requirements.txt

- main.py
- word-based-cards
  - generate_csv.py
  - make_anki_pkg.py
  - import_to_anki.py
  - create_text_files.py
  - words.txt

## Notes

- Be sure to set your OpenAI API key in a `.env` file.
- If using AnkiConnect to automatically import cards into Anki update the ANKI_CONNECT_URL in the `.env` file to the local address of AnkiConnect.

## License

MIT
