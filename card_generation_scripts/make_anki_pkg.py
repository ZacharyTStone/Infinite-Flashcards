import csv
import os
import genanki

def import_to_anki(csv_file_path, deck_name):
    # Define the Anki model with CSS
    model = genanki.Model(
        1607392319,  # Random model ID
        'Japanese Word Model',
        fields=[
            {'name': 'Word'},
            {'name': 'Word_Reading'},
            {'name': 'Example Sentence 1'},
            {'name': 'Example Sentence 2'},
            {'name': 'Translation'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '''
                    <div class="wrap">
                        <div class="fside">{{FrontSide}}</div>

                        <div class="sent-center">
                            <div class="jpsentence" lang="ja">
                                {{Example Sentence 1}}
                            </div>
                        </div>
                    </div>
                ''',
                'afmt': '''
                    <div class="wrap">
                        <div class="fside">{{Word}} | {{Word_Reading}}</div>

                        <div class="sent-center">
                            <div class="jpsentence" lang="ja">
                                1. {{Example Sentence 1}}<br>
                                2. {{Example Sentence 2}}
                            </div>
                            <div class="ensentence" lang="en">{{Translation}}</div>
                        </div>
                        <footer>
                            <a title="Translate with Google Translate" target="_blank"
                                href="https://translate.google.com/?hl=en&sl=ja&tl=en&text={{Word}}&op=translate">Translate</a>
                            <a href="https://jisho.org/search?keyword={{Word}}" title="Word on Jisho">English Dictionary</a>
                            <a href="https://dictionary.goo.ne.jp/srch/all/{{Word}}/m0u/" title="Word on Japanese Dictionary">Japanese Dictionary</a>
                            <a href="https://www.google.co.jp/search?q={{Word}}&tbm=isch" title="Search images">Images</a>
                        </footer>
                    </div>
                '''
            }
        ],
        css='''
            .wrap {
                color: white;
                background-color: #2e2e2e;
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                margin-bottom: 30px; 
            }

            .fside {
                font-size: 30px;
                font-weight: bold;
                margin-bottom: 20px; 
            }

            .sent-center {
                margin-top: 20px;
                font-size: 20px;
                margin-bottom: 20px;
            }

            .jpsentence {
                font-family: "Noto Serif", "Noto Serif CJK JP", Yu Mincho, "Liberation Serif", "Times New Roman", Times, Georgia, Serif;
                margin-bottom: 20px; 
            }

            .ensentence {
                margin-top: 10px;
                color: #a0a0a0;
                margin-bottom: 20px; 
            }

            footer {
                margin-top: 20px;
                text-align: center;
                margin-bottom: 20px;
            }

            footer a {
                color: #4a90e2;
                margin-right: 10px;
            }

            .card {
                background-color: #2e2e2e;
                color: white;
                margin-bottom: 30px; 
            }
        '''
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
                    row['Word_Reading'],
                    row['Example Sentence 1'],
                    row['Example Sentence 2'],
                    row['Translation'],
                ])
            deck.add_note(note)

    # Create Anki package
    package = genanki.Package(deck)
    package.write_to_file(f'{deck_name}.apkg')

    # Move the apkg file to the correct directory ./files
    os.rename(f'{deck_name}.apkg', f'./files/{deck_name}.apkg')

    print(f'Anki package "{deck_name}.apkg" created successfully.')

# Replace 'Japanese_Word_Examples.csv' with the path to your CSV file
csv_file_path = './files/Japanese_Word_Examples.csv'

# Log csv file path
print(csv_file_path)

# Replace 'Japanese Words' with the desired name for your Anki deck
deck_name = 'Japanese_AI_Vocab_Deck'

import_to_anki(csv_file_path, deck_name)
