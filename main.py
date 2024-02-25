import asyncio
import subprocess
import os

async def run_script(script):
    proc = await asyncio.create_subprocess_exec('python3', script)
    await proc.wait()

async def main(folder):
    if folder == 1:
        folder_name = "word-based-cards"
    elif folder == 2:
        folder_name = "essay-based-cards"
    elif folder == 3:
        folder_name = "sentence-based-cards"
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        return

    folder_path = os.path.join(os.getcwd(), folder_name)
    os.chdir(folder_path)

    # List of scripts to run
    scripts = ['generate_csv.py', 'make_anki_pkg.py', 'import_to_anki.py']

    # Run scripts sequentially
    for script in scripts:
        await run_script(script)

# Get user input for the folder choice
folder_choice = input("Enter 1 for 'word-based-cards', 2 for 'essay-based-cards', or 3 for 'sentence-based-cards': ")

# Run the main coroutine
asyncio.run(main(int(folder_choice)))
