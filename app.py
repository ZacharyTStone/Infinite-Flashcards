from flask import Flask, request, render_template
import asyncio
import os

app = Flask(__name__)

async def run_script(script):
    proc = await asyncio.create_subprocess_exec('python3', script)
    await proc.wait()

async def main(language):
    if language == "1":
        card_language = 'Japanese'
    else:
        return "Invalid language choice."

    folder_path = os.path.join(os.getcwd(), 'word-based-cards')
    os.chdir(folder_path)

    with open('files/language_choice.txt', 'w') as file:
        file.write(str(card_language))

    scripts = ['generate_csv.py', 'make_anki_pkg.py', 'import_to_anki.py']
    for script in scripts:
        await run_script(script)
    return "Scripts executed successfully."

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        language_choice = request.form['language']
        words_input = request.form['words']  # 複数の単語を取得

        # 複数の単語をwords.txtファイルに追加
        with open('words.txt', 'a') as file:
            file.write(words_input + '\n')

        # print words file
        with open('words.txt', 'r') as file:
            print(file.read())
        result = asyncio.run(main(language_choice))
        return result
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)