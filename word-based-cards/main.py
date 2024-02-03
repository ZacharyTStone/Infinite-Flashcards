import asyncio
import subprocess

async def run_script(script):
    proc = await asyncio.create_subprocess_exec('python3', script)
    await proc.wait()

async def main():
    # List of scripts to run
    scripts = ['generate_csv.py', 'make_anki_pkg.py', 'import_to_anki.py']

    # Run scripts sequentially
    for script in scripts:
        await run_script(script)

# Run the main coroutine
asyncio.run(main())
