import asyncio
import subprocess
import os

async def run_script(script):
    proc = await asyncio.create_subprocess_exec('python3', script)
    await proc.wait()

async def main(language):
    if language == 1:
        card_language = 'Japanese'
    else:
        print("Invalid language choice.")
        return

    folder_path = os.path.join(os.getcwd(), 'word-based-cards')
    os.chdir(folder_path)

    # add the language choice as a text file in the files folder so that the other scripts can read it
    # make a new folder/file if it doesn't exist
    
    
    with open('files/language_choice.txt', 'w') as file:
        file.write(str(card_language))


    # List of scripts to run
    scripts = ['generate_csv.py', 'make_anki_pkg.py', 'import_to_anki.py']

    # Run scripts sequentially
    for script in scripts:
        await run_script(script)

# Get user input for the language choice
language_choice = input("Enter 1 for Japanese (Currently only Japanese is supported) ").strip()

# Run the main coroutine
asyncio.run(main(int(language_choice)))
