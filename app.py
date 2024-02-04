import subprocess
import asyncio
import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    script_type = request.form['script_type']
    if script_type == 'essay':
        asyncio.run(run_essay_main())
    elif script_type == 'word':
        asyncio.run(run_word_main())
    elif script_type == 'sentence':
        asyncio.run(run_sentence_main())
    return 'Script executed successfully!'

async def run_essay_main():
    await run_script_in_folder('essay_based_cards')

async def run_word_main():
    await run_script_in_folder('word_based_cards')
    await create_words_txt('word_based_cards')

async def run_sentence_main():
    await run_script_in_folder('sentence_based_cards')
    await create_words_txt('sentence_based_cards')

async def run_script_in_folder(folder_name):
    script_path = f'{folder_name}/main.py'
    proc = await asyncio.create_subprocess_exec('python3', script_path)
    await proc.wait()

async def create_words_txt(folder_name):
    subfolders = [os.path.join(folder_name, name) for name in os.listdir(folder_name) if os.path.isdir(os.path.join(folder_name, name))]
    textname = ''
    if folder_name == 'word_based_cards':
        textname = 'words.txt'
    elif folder_name == 'sentence_based_cards':
        textname = 'sentences.txt'
    else:
        textname = 'essay.txt'

    for subfolder in subfolders:
        words_txt_path = os.path.join(subfolder, (textname))
        if not os.path.exists(words_txt_path):
            with open(words_txt_path, 'w') as f:
                f.write('')  # Creating an empty file

if __name__ == '__main__':
    app.run(debug=True)
