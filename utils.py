import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def import_deck(deck_path, name_of_text_file):
    # AnkiConnect endpoint URL to import the deck
    anki_url = os.getenv("ANKI_CONNECT_URL")

    # Get the absolute path of the deck file
    absolute_deck_path = os.path.abspath(deck_path)

    # Import deck request parameters
    params = {
        "action": "importPackage",
        "params": {
            "path": absolute_deck_path
        }
    }

    # Send POST request to AnkiConnect
    response = requests.post(anki_url, json=params)

    # Check if the request was successful
    if response.status_code == 200:
        print("Deck imported successfully.")

        # Delete all files in the files directory at the same level as this script
        for file in os.listdir("./files"):
            file_path = os.path.join("./files", file)
            if os.path.isfile(file_path):
                os.remove(file_path)

        # Delete the txt file at the same level as this script
        if os.path.exists("../" + name_of_text_file + ".txt"):
            os.remove("../" + name_of_text_file + ".txt")
        else:
            print("The file does not exist. Please clear your text file manually before running the script again.")

        # Make a new txt file
        with open("../" + name_of_text_file + ".txt", "w") as file:
            file.write("")
    else:
        print("Failed to import deck.")

def check_word_count(words, limit=10):
    if len(words) > limit:
        raise ValueError(f"The number of words exceeds {limit}. Please enter {limit} or fewer words.")

