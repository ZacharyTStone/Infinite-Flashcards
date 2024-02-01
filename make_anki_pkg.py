import csv
import os
import genanki

def import_to_anki(csv_file_path, deck_name):
    # Define the Anki model
    model = genanki.Model(
        1607392319,  # Random model ID
        'Japanese Word Model',
        fields=[
            {'name': 'Word'},
            {'name': 'Hiragana'},
            {'name': 'Example Sentence 1'},
            {'name': 'Example Sentence 2'},
            {'name': 'English Translation'}
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '''
                    <div id="header">
                        <p>
                            <i>{{Word}}</i>
                        </p>
                        <hr>
                        <p>{{Example Sentence 1}}</p>
                        <p>{{Example Sentence 2}}</p>
                    </div>
                ''',
                'afmt': '''
                    <div id="header">
                        <p>
                            <i>{{Word}} | {{Hiragana}}</i>
                        </p>
                        <hr>
                              <p>{{English Translation}}</p>
                        <hr>
                        <p>1.{{Example Sentence 1}}</p>
                        <p>2.{{Example Sentence 2}}</p>
                        <hr>
                        <p>{{English Translation}}</p>
                    </div>
                '''
            }
        ]
    )


    # Create a new Anki deck
    deck = genanki.Deck(
        2059400110,  # Random deck ID
        deck_name)

    # Read data from CSV and add to Anki deck
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            note = genanki.Note(
                model=model,
                fields=[
                    row['Word'],
                    row['Hiragana'],
                    row['Example Sentence 1'],
                    row['Example Sentence 2'],
                    row['English Translation']
                ])
            deck.add_note(note)

    # Create Anki package
    package = genanki.Package(deck)
    package.write_to_file(f'{deck_name}.apkg')

    # move the apkg file to the correct directory ./files
    os.rename(f'{deck_name}.apkg', f'./files/{deck_name}.apkg')

    print(f'Anki package "{deck_name}.apkg" created successfully.')

# Replace 'Japanese_Word_Examples.csv' with the path to your CSV file
csv_file_path = './files/Japanese_Word_Examples.csv'

# Replace 'Japanese Words' with the desired name for your Anki deck
deck_name = 'Japanese_AI_Vocab_Deck'

import_to_anki(csv_file_path, deck_name)
