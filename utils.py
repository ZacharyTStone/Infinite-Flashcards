import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def clear_and_create_file(directory, name_of_text_file):
    # # Delete all files in the specified directory
    # for file in os.listdir(directory):
    #     file_path = os.path.join(directory, file)
    #     if os.path.isfile(file_path):
    #         os.remove(file_path)

    # # Delete the txt file
    # txt_file_path = os.path.join(name_of_text_file + ".txt")
    
    # if os.path.exists(txt_file_path):
    #     os.remove(txt_file_path)
    # else:
    #     print("The file does not exist. Please clear your text file manually before running the script again.")

    # # Make a new txt file
    # with open(txt_file_path, "w") as file:
    #     file.write("")

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

        # Use the new utility function
        clear_and_create_file('./files', "words")
    else:
        print("Failed to import deck.")

