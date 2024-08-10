import os
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import sys
import csv
# Add the parent directory of the current file to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import remove_duplicates
# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

from image_search import search_image

CSV_FILENAME = "Japanese_Word_Examples.csv"

def write_to_csv(data, filename=CSV_FILENAME):
    # Ensure the 'files' directory exists
    os.makedirs('./files', exist_ok=True)
    
    # Create the full path for the CSV file
    csv_path = os.path.join('./files', filename)
    
    # Convert rows into a pandas DataFrame
    df = pd.DataFrame(data, columns=["Word", "Word_Reading", "Example Sentence 1", "Example Sentence 2", "Translation", "Front_Image_URL", "Back_Image_URL"])
    
    # Write the DataFrame to CSV
    df.to_csv(csv_path, index=False)
    print(f"CSV file created: {csv_path}")

def generate_explanations(words):
    language = 'Japanese'
    print('language:', language)    

    # Construct the prompt dynamically based on the number of words
    system_message = f"You are a {language} teacher. You will generate natural sounding, easy to understand, Japanese {language} explanations for the given words, following the format EXACTLY."
    
    user_message = "Words to explain:\n"
    for i, word in enumerate(words, start=1):
        user_message += f"{i}. {word}\n"

    user_message += "\nStrict Format: <word> | <hiragana>(NHK pitch accent) | <example sentance 1> | <example sentance 2> | <definition>\n"
    user_message += "Critical Rules:\n"
    user_message += "- Exactly 5 fields per word, separated by | symbol\n"
    user_message += "- One word per line\n"
    user_message += "- Use N/A for any unavailable information\n"
    user_message += "- No deviations from this format allowed\n"
    user_message += "- Ensure accuracy, especially for NHK pitch accent\n"
    user_message += "- Ensure the example sentences are natural, used by real Japanese people, and give a good understanding of the word.\n"
    user_message += "Example (follow this format precisely):\n"
    user_message += "食べ物 | たべもの(2) | 食べ物が好きです。 | の���の食べ物はとても美味しいです。 | 食用にするもの。また、飲み物に対して、噛んで食べるもの。しょくもつ。 \n"

    # Send prompt to OpenAI API
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ],
        temperature=0.5,
        max_tokens=3000,
        top_p=1,
        frequency_penalty=0.3,
        presence_penalty=0,
    )

    print('prompt:', user_message)

    # Get the response content
    response_content = response.choices[0].message.content

    # Split the response text by newline and filter out any empty lines
    data = [line.strip() for line in response_content.strip().split("\n") if line.strip()]
    
    # Check if each line contains five fields separated by pipe symbol
    for i, line in enumerate(data):
        fields = line.split(" | ")
        if len(fields) != 5:
            print(f"Warning: Unexpected format in line {i+1}. Expected 5 fields, but found {len(fields)} fields. Fixing...")
            # Pad or truncate fields to ensure five fields
            data[i] = " | ".join(fields[:5]).ljust(5, " ")
    
    # Search for images
    for i, line in enumerate(data):
        word, word_reading, example_sentence_1, example_sentence_2, translation = line.split(" | ")
        image_urls = search_image(word, num_results=2)
        front_image_url = image_urls[0] if image_urls else ""
        back_image_url = image_urls[1] if len(image_urls) > 1 else front_image_url
        data[i] = [word, word_reading, example_sentence_1, example_sentence_2, translation, front_image_url, back_image_url]

    return data

def read_words_from_file(file_path):
    words = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line:  # Exclude empty lines
                    words.extend(stripped_line.split())  # Split words separated by spaces into individual lines
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except IOError:
        print(f"Error reading file: {file_path}")
    return remove_duplicates(words)

def main():
    # Read words from text file
    words = read_words_from_file("words.txt")

    print('words:', words)

    # Generate explanations 
    data = []
    for i in range(0, len(words), 3):
        data.extend(generate_explanations(words[i:i+3]))
    
    print(data)

    # Create CSV file
    write_to_csv(data)

if __name__ == "__main__":
    try:
        main()
    except ValueError:
        pass  # Do nothing and exit gracefully