import sys
import os
import requests
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from variables import ANKI_DECK_NAME, DECK_PATH, NAME_OF_TEXT_FILE, ANKI_CONNECT_URL

def main():
    if not os.path.exists(DECK_PATH):
        print(f"Error: Anki deck file not found at {DECK_PATH}")
        return

    print(f"Attempting to import deck from {DECK_PATH}")
    
    params = {
        "action": "importPackage",
        "version": 6,
        "params": {
            "path": os.path.abspath(DECK_PATH)
        }
    }

    try:
        response = requests.post(ANKI_CONNECT_URL, json=params)
        response.raise_for_status()
        result = response.json()
        
        if result.get('error'):
            print(f"Error importing deck: {result['error']}")
        else:
            print(f"Deck imported successfully. Response: {result}")
            
            # Check if the deck exists after import
            check_params = {
                "action": "deckNames",
                "version": 6
            }
            check_response = requests.post(ANKI_CONNECT_URL, json=check_params)
            check_response.raise_for_status()
            deck_names = check_response.json()['result']
            
            if ANKI_DECK_NAME in deck_names:
                print(f"Deck '{ANKI_DECK_NAME}' found in Anki after import.")
            else:
                print(f"Warning: Deck '{ANKI_DECK_NAME}' not found in Anki after import.")
        
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to AnkiConnect: {e}")

if __name__ == "__main__":
    main()