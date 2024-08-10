import asyncio
import subprocess
import os
import sys
import logging

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from variables import CSV_FILE_PATH, CSV_FILE_PATH_WITH_IMAGES, CSV_FILE_PATH_WITH_AUDIO, ANKI_DECK_NAME, DECK_PATH, NAME_OF_TEXT_FILE, API_KEY, CSV_FILENAME

logging.basicConfig(level=logging.INFO)

async def run_script(script):
    try:
        proc = await asyncio.create_subprocess_exec('python3', script,
                                                    stdout=asyncio.subprocess.PIPE,
                                                    stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await proc.communicate()
        
        if stdout:
            logging.info(f"{script} output:\n{stdout.decode()}")
        if stderr:
            logging.error(f"{script} error:\n{stderr.decode()}")
        
        if proc.returncode != 0:
            logging.error(f"Error: {script} exited with code {proc.returncode}")
            return False
        return True
    except Exception as e:
        logging.error(f"Error running {script}: {e}")
        return False

def create_blank_files():
    base_path = os.path.dirname(__file__)
    files = [os.path.join(base_path, 'card_generation_scripts', 'words.txt')]

    for file in files:
        with open(file, 'w') as f:
            pass

async def main():
    original_dir = os.getcwd()
    folder_path = os.path.join(original_dir, 'card_generation_scripts')
    
    # Ensure the 'files' directory exists
    os.makedirs('./files', exist_ok=True)
    os.makedirs('./files/images', exist_ok=True)
    
    if not os.path.exists(os.path.join(folder_path, 'words.txt')):
        create_blank_files()
        print("Words.txt created successfully. You can now add words to it in the card_generation_scripts folder.")
        return

    os.chdir(folder_path)

    scripts = ['generate_csv.py', 'download_images.py', 'generate_audio.py', 'make_anki_pkg.py', 'import_to_anki.py']
    for script in scripts:
        success = await run_script(script)
        if not success:
            print(f"Error occurred in {script}. Stopping execution.")
            break

    os.chdir(original_dir)

if __name__ == "__main__":
    asyncio.run(main())