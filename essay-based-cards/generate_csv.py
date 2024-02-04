import os
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def create_csv_file(data):
    # Split the returned data into separate rows and adjust each row to have five fields
    rows = [row.split(" | ")[:5] for row in data]

    # Convert rows into a pandas DataFrame
    df = pd.DataFrame(rows, columns=["Word", "Hiragana", "Example Sentence 1", "Example Sentence 2", "English Translation"])

    # Save DataFrame to a CSV file
    df.to_csv("Japanese_Word_Examples.csv", index=False)
    print("CSV file created successfully!")

def generate_explanations(essay):
    # Construct the prompt dynamically based on the number of essay

    prompt = "analyze the words in the following essay. Please find the 5-10 most difficult Japanese words. If you are unsure of difficulty please check if they are in the JLPT N1 level. Then give output about the words in the format below\n"

    prompt += "\n Format the output of the picked words as follows:\n<word>  | <word in hiragana> | <full sentance in essay> | <example sentence using the word> | <dictionary defintion of the word in Japanese>\n\nWarning: Ensure that the output strictly adheres to the specified format. Any deviation from the format will not be acceptable. each word should have the 5 fields separated by a pipe (|) symbol. Each word should be on a new line. the first field should be the word, the second the word in hiragna, the third is the word used in the essay sentance, the fourth should be a Japanese example sentance using the word, the fifth and last section should be a direct Japanse translation of the word. You must put something for each section. if you can not find anything put N/A"

    prompt += "\n Example: 食べ物  | たべもの | 食べ物が好きです。 | この店の食べ物はとても美味しいです。 | 食物をかんで、のみこむ。\n\n"

    prompt += "\n Only make sure to include words that are JLPT N1 level. You can ignore any words that are not JLPT N1 level."

    prompt += "\n Essay: \n\n"
    
    prompt+= essay

    # Send prompt to OpenAI API
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=500,
    )

    # Split the response text by newline and filter out any empty lines
    data = [line.strip() for line in response.choices[0].text.strip().split("\n") if line.strip()]
    
    # Check if each line contains five fields separated by pipe symbol
    for i, line in enumerate(data):
        fields = line.split(" | ")
        if len(fields) != 5:
            print(f"Warning: Unexpected format in line {i+1}. Expected 5 fields, but found {len(fields)} fields. Fixing...")
            # Pad or truncate fields to ensure five fields
            data[i] = " | ".join(fields[:5]).ljust(5, " ")
    
    return data

# use csv instead of excel for anki. If you want to use excel, you can use the following code

# def create_excel_sheet(data):
#     # Split the returned data into separate rows and adjust each row to have five fields
#     rows = [row.split(" | ")[:5] for row in data]

#     # Convert rows into a pandas DataFrame
#     df = pd.DataFrame(rows, columns=["Word", "Hiragana", "Example Sentence 1", "Example Sentence 2", "English Translation"])

#     # Save DataFrame to an Excel spreadsheet
#     df.to_excel("Japanese_Word_Examples.xlsx", index=False)
#     print("Excel spreadsheet created successfully!")

def main():
    # Read Essay from text file
    with open("essay.txt", "r", encoding="utf-8") as file:
        essay = file.read()

    # Generate explanations for the essay
    data = generate_explanations(essay)

    print(data) # Print the data to the console

    # Create CSV file
    create_csv_file(data)

    # move the csv file to the correct directory ./files

    # check if the directory exists
    if not os.path.exists("./files"):
        os.makedirs("./files")

    os.rename("Japanese_Word_Examples.csv", "./files/Japanese_Word_Examples.csv")

    # Create Excel spreadsheet
    # create_excel_sheet(data)

if __name__ == "__main__":
    main()
