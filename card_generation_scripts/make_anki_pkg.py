import csv
import os
import genanki
from dotenv import load_dotenv

load_dotenv()

csv_file_path = './files/Japanese_Word_Examples_With_Audio.csv'

def import_to_anki(csv_file_path, deck_name):
    model = genanki.Model(
        1607392319,
        'Japanese Word Model',
        fields=[
            {'name': 'Word'},
            {'name': 'Word_Reading'},
            {'name': 'Example Sentence 1'},
            {'name': 'Example Sentence 2'},
            {'name': 'Translation'},
            {'name': 'Word_Audio'},
            {'name': 'Example_Sentence_1_Audio'},
            {'name': 'Dictionary_Definition_Audio'}
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
                        <div class="fside">{{Word}} | {{Word_Reading}} {{Word_Audio}}</div>

                        <div class="sent-center">
                            <div class="jpsentence" lang="ja">
                                1. {{Example Sentence 1}} {{Example_Sentence_1_Audio}}<br>
                                2. {{Example Sentence 2}}
                            </div>
                            <div class="ensentence" lang="en">{{Translation}} {{Dictionary_Definition_Audio}}</div>
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
                font-size: 2rem;
                font-weight: bold;
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

    deck = genanki.Deck(
        2059400110,
        deck_name)

    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            word = row['Word']
            reading = row['Word_Reading']
            sentence1 = row['Example Sentence 1']
            sentence2 = row['Example Sentence 2']
            translation = row['Translation']
            word_audio = row['Word_Audio']
            example_sentence_1_audio = row['Example_Sentence_1_Audio']
            dictionary_definition_audio = row['Dictionary_Definition_Audio']

            note = genanki.Note(
                model=model,
                fields=[
                    word,
                    reading,
                    sentence1,
                    sentence2,
                    translation,
                    word_audio,
                    example_sentence_1_audio,
                    dictionary_definition_audio
                ])
            deck.add_note(note)

    audio_files = [os.path.join('./files', f) for f in os.listdir('./files') if os.path.isfile(os.path.join('./files', f)) and f.endswith('.mp3')]

    package = genanki.Package(deck)
    package.media_files = audio_files
    package.write_to_file(f'./files/{deck_name}.apkg')

    print(f'Anki package "{deck_name}.apkg" created successfully.')

deck_name = os.getenv("ANKI_DECK_NAME", "Japanese_AI_Vocab_Deck")
import_to_anki(csv_file_path, deck_name)
