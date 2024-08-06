import sys
import os

# Add the parent directory of the current file to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import import_deck
from variables import ANKI_DECK_NAME  # Import the variable from variables.py


# Set the deck name and file paths
deck_name = ANKI_DECK_NAME
deck_path = f"./files/{deck_name}.apkg"
name_of_text_file = "words"

# Call the function to import the deck
# This function is likely defined in the utils.py file
import_deck(deck_path, name_of_text_file)