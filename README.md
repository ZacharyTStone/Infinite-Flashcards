# OpenAI Anki Card Generator

This project is a Python script that generates Anki cards from a word list or essay using OpenAI. The generated cards include hiragana, example sentences, and basic Japanese definitions.

## Features

- Word-based card generation
- Essay-based card generation
- Option to generate CSV files or Excel files
- Generation and import of Anki packages (.apkg) using AnkiConnect

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

## Usage

- To generate word-based cards, run `word-based-cards/main.py`.
- To generate essay-based cards, run `essay-based-cards/main.py`.

## Project Structure

```
.
├── .env
├── .gitignore
├── README.md
├── essay-based-cards
│   ├── generate_csv.py
│   ├── import_to_anki.py
│   ├── make_anki_pkg.py
│   └── main.py
└── word-based-cards
    ├── generate_csv.py
    ├── import_to_anki.py
    ├── make_anki_pkg.py
    └── main.py
```

## Notes

- Be sure to set your OpenAI API key in the `.env` file.
- If using AnkiConnect to automatically import cards into Anki, ensure the the local address in `import_to_anki.py` is correct.

## License

MIT
