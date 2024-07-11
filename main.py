import asyncio
import subprocess
import os
from variables import CSV_FILE_PATH, ANKI_DECK_NAME, DECK_PATH, NAME_OF_TEXT_FILE, API_KEY, CSV_FILENAME

async def run_script(script):
    proc = await asyncio.create_subprocess_exec('python3', script)
    await proc.wait()

def create_blank_files():
    base_path = os.path.dirname(__file__)
    files = [os.path.join(base_path, 'words.txt')]

    for file in files:
        with open(file, 'w') as f:
            pass

async def main():
    folder_path = os.path.join(os.getcwd(), 'card_generation_scripts')
    os.chdir(folder_path)

    if not os.path.exists('words.txt'):
        create_blank_files()
        print("Words.txt created successfully. you can now add words to it in the card_generation_scripts folder.")
        return

    scripts = ['generate_csv.py', 'generate_audio.py', 'make_anki_pkg.py', 'import_to_anki.py']
    for script in scripts:
        await run_script(script)

asyncio.run(main())