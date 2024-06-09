import asyncio
import subprocess
import os

async def run_script(script):
    proc = await asyncio.create_subprocess_exec('python3', script)
    await proc.wait()

async def main():


    folder_path = os.path.join(os.getcwd(), 'card_generation_scripts')

    os.chdir(folder_path)

    # check if words.txt exists in card_generation_scripts
    # if it doesn't exist, create it with the script create_text_files.py in card_generation_scripts
    if not os.path.exists('words.txt'):
        await run_script('create_text_files.py')
        # get out of the main function
        return

   

    # List of scripts to run
    scripts = ['generate_csv.py', 'generate_audio.py', 'make_anki_pkg.py', 'import_to_anki.py']

    # Run scripts sequentially
    for script in scripts:
        await run_script(script)


# Run the main coroutine
asyncio.run(main())
