from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# utils.py
ANKI_CONNECT_URL = os.getenv("ANKI_CONNECT_URL")

# card_generation_scripts/make_anki_pkg.py
CSV_FILE_PATH = './files/Japanese_Word_Examples_With_Audio.csv'

# card_generation_scripts/import_to_anki.py
ANKI_DECK_NAME = os.getenv("ANKI_DECK_NAME", "Japanese_AI_Vocab_Deck")
DECK_PATH = f"./files/{ANKI_DECK_NAME}.apkg"
NAME_OF_TEXT_FILE = "words"

# card_generation_scripts/generate_csv.py
API_KEY = os.getenv("OPENAI_API_KEY")
CSV_FILENAME = "Japanese_Word_Examples.csv"