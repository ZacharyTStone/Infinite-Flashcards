import os
import sys
import csv
import genanki

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from variables import CSV_FILE_PATH_WITH_AUDIO, DECK_PATH, ANKI_DECK_NAME

def create_anki_deck():
    if not os.path.exists(CSV_FILE_PATH_WITH_AUDIO):
        print(f"Error: CSV file not found at {CSV_FILE_PATH_WITH_AUDIO}")
        return

    # Create Anki deck
    deck = genanki.Deck(2059400110, ANKI_DECK_NAME)

    # Define the note model with simplified templates
    model = genanki.Model(
        1607392319,
        'Japanese Vocab Model',
        fields=[
            {'name': 'Word'},
            {'name': 'Reading'},
            {'name': 'Example1'},
            {'name': 'Example2'},
            {'name': 'Definition'},
            {'name': 'FrontImage'},
            {'name': 'BackImage'},
            {'name': 'WordAudio'},
            {'name': 'Example1Audio'},
            {'name': 'DefinitionAudio'}
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '''
                    Word: {{Word}}<br>
                    Front Image: {{FrontImage}}<br>
                ''',
                'afmt': '''
                    {{FrontSide}}
                    <hr id="answer">
                    Reading: {{Reading}}<br>
                    Example 1: {{Example1}}<br>
                    Example 2: {{Example2}}<br>
                    Definition: {{Definition}}<br>
                    Back Image: {{BackImage}}<br>
                    Word Audio: {{WordAudio}}<br>
                    Example Audio: {{Example1Audio}}<br>
                    Definition Audio: {{DefinitionAudio}}<br>
                ''',
            },
        ])

    # Read CSV and create notes
    with open(CSV_FILE_PATH_WITH_AUDIO, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            if len(row) < 10:
                print(f"Warning: Skipping row due to insufficient data: {row}")
                continue
            
            word, reading, example_1, example_2, definition, front_image, back_image, word_audio, example_1_audio, definition_audio = row[:10]
            
            # Print out the data for each note
            print(f"Creating note with data:")
            print(f"Word: {word}")
            print(f"Reading: {reading}")
            print(f"Example 1: {example_1}")
            print(f"Example 2: {example_2}")
            print(f"Definition: {definition}")
            print(f"Front Image: {front_image}")
            print(f"Back Image: {back_image}")
            print(f"Word Audio: {word_audio}")
            print(f"Example 1 Audio: {example_1_audio}")
            print(f"Definition Audio: {definition_audio}")
            print("---")
            
            note = genanki.Note(
                model=model,
                fields=[word, reading, example_1, example_2, definition, front_image, back_image, word_audio, example_1_audio, definition_audio]
            )
            deck.add_note(note)

    # Create and save the Anki package
    package = genanki.Package(deck)
    package.write_to_file(DECK_PATH)

    print(f"Anki deck created: {DECK_PATH}")

if __name__ == "__main__":
    create_anki_deck()