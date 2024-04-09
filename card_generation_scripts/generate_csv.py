import os
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)



def get_first_image_url(search_term, api_key, cx):
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': search_term,
        'cx': cx,
        'key': api_key,
        'searchType': 'image',
    }
    response = requests.get(search_url, params=params)
    result = response.json()


    def find_image_src(obj, depth=0):
        if depth > 10:
            return None
        if isinstance(obj, dict):
            if 'cse_image' in obj and 'src' in obj['cse_image']:
                return obj['cse_image']['src']
            elif 'cse_thumbnail' in obj and 'src' in obj['cse_thumbnail']:
                return obj['cse_thumbnail']['src']
            for key in obj:
                found = find_image_src(obj[key], depth + 1)
                if found:
                    return found
        elif isinstance(obj, list):
            for item in obj:
                found = find_image_src(item, depth + 1)
                if found:
                    return found
        return None

    image_src = find_image_src(result)
    return image_src if image_src else "N/A"
# APIキーとCSE IDを設定
img_api_key = os.getenv("IMG_API_KEY")
img_cx = os.getenv("IMG_CX")


def write_to_csv(data, filename="Japanese_Word_Examples.csv"):
    # Split the returned data into separate rows and adjust each row to have five fields
    rows = [row.split(" | ")[:6] for row in data]

    # Convert rows into a pandas DataFrame
    df = pd.DataFrame(rows, columns=["Word", "Word_Reading", "Example Sentence 1", "Image URL", "Example Sentence 2", "Translation"])

    # Save DataFrame to a CSV file
    df.to_csv(filename, index=False)
    print("CSV file created successfully!")

def generate_explanations(words):
    
    language = 'Japanese'

    print('language:', language)    

    # Construct the prompt dynamically based on the number of words
    prompt = f"Generate explanations and example sentences in {language} for the following words in the format specified:\n"
    for i, word in enumerate(words, start=1):
        prompt += f"{i}. {word}\n"

    prompt += "\n Format the output as follows:\n<word>  | <word in hiragana> | <example sentence 1> | <example sentence 2> | <dictionary definition in {language}>\n\nWarning: Ensure that the output strictly adheres to the specified format. Any deviation from the format will not be acceptable. each word should have the 5 fields separated by a pipe (|) symbol. Each word should be on a new line. the first field should be the word, the second the word in hiragna, the third a {language} example sentence using the word, the fourth should be a {language} example sentence using the word, the fifth and last section should be a direct {language} definition of the word. You must put something for each section. if you can not find anything put N/A and a pipe to start the next field"

    prompt += "\n Example You have to follow when responding: 食べ物  | たべもの | 食べ物が好きです。 | この店の食べ物はとても美味しいです。 | 食物をかんで、のみこむ。\n\n"
    # Send prompt to OpenAI API
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0,
        max_tokens=3700,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    print('prompt:', prompt)

    # Split the response text by newline and filter out any empty lines
    data = [line.strip() for line in response.choices[0].text.strip().split("\n") if line.strip()]
    
    # Check if each line contains five fields separated by pipe symbol
    for i, line in enumerate(data):
        fields = line.split(" | ")
        if len(fields) != 5:
            print(f"Warning: Unexpected format in line {i+1}. Expected 5 fields, but found {len(fields)} fields. Fixing...")
            # Pad or truncate fields to ensure five fields
            data[i] = " | ".join(fields[:5]).ljust(5, " ")
    
    # Insert image URL after the first example sentence
    updated_data = []

    for line in data:
        fields = line.split(" | ")
        if len(fields) == 5:
            image_url = get_first_image_url(fields[0], img_api_key, img_cx)
            fields.insert(2, image_url)
            updated_line = " | ".join(fields)
            updated_data.append(updated_line)
        else:
            updated_data.append(line)
    
    return updated_data


def main():
    # Read words from text file
    with open("words.txt", "r", encoding="utf-8") as file:
        words = [word.strip() for word in file.readlines()]

    # Check if the number of words exceeds the limit
    # check_word_count(words)

    print('words:', words)

    # Generate explanations 

    # we need to do 5 words at a time and combine the results
   
    data = []

    for i in range(0, len(words), 5):
        data.extend(generate_explanations(words[i:i+5]))
    
    print(data)

    # Create CSV file
    write_to_csv(data)

    # Check if the directory exists
    if not os.path.exists("./files"):
        os.makedirs("./files")

    # Move the CSV file to the correct directory ./files
    os.rename("Japanese_Word_Examples.csv", "./files/Japanese_Word_Examples.csv")

if __name__ == "__main__":
    try:
        main()
    except ValueError:
        pass  # Do nothing and exit gracefully
