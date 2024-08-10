from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# utils.py
ANKI_CONNECT_URL = os.getenv("ANKI_CONNECT_URL")

# card_generation_scripts/make_anki_pkg.py
CSV_FILE_PATH = os.path.join('./files', 'Japanese_Word_Examples.csv')
CSV_FILE_PATH_WITH_IMAGES = os.path.join('./files', 'Japanese_Word_Examples_with_images.csv')
CSV_FILE_PATH_WITH_AUDIO = os.path.join('./files', 'Japanese_Word_Examples_with_audio.csv')

# card_generation_scripts/import_to_anki.py
ANKI_DECK_NAME = os.getenv("ANKI_DECK_NAME", "Japanese_AI_Vocab_Deck")
DECK_PATH = os.path.join('./files', f"{ANKI_DECK_NAME}.apkg")
NAME_OF_TEXT_FILE = "words"

# card_generation_scripts/generate_csv.py
API_KEY = os.getenv("OPENAI_API_KEY")
CSV_FILENAME = "Japanese_Word_Examples.csv"

# Google Custom Search API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

# Unsplash API
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")