import openai
import pandas as pd

# OpenAI API key
api_key = 'your-api-key'  # Replace 'your-api-key' with your actual API key
openai.api_key = api_key

def generate_explanations(words):
    # Format words into the prompt
    prompt = f"""Generate explanations and example sentences in Japanese for the following words:\n1. {words[0]}\n2. {words[1]}\n3. {words[2]}\n4. {words[3]}\n5. {words[4]}\n6. {words[5]}\n7. {words[6]}\n8. {words[7]}\n9. {words[8]}\n10. {words[9]}\n\nFormat the output as follows:\n<word>  | <word in hiragana> | <example sentence 1> | <example sentence 2> | <translation in English>\n\nWarning: Ensure that the output strictly adheres to the specified format. Any deviation from the format will not be acceptable."""

    # Send prompt to OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=300
    )

    return response.choices[0].text.strip().split("\n")

def create_excel_sheet(data):
    # Split the returned data into separate rows
    rows = [row.split(" | ") for row in data]

    # Convert rows into a pandas DataFrame
    df = pd.DataFrame(rows, columns=["Word", "Hiragana", "Example Sentence 1", "Example Sentence 2", "English Translation"])

    # Save DataFrame to an Excel spreadsheet
    df.to_excel("Japanese_Word_Examples.xlsx", index=False)
    print("Excel spreadsheet created successfully!")

def main():
    # Read words from text file
    with open("words.txt", "r", encoding="utf-8") as file:
        words = [word.strip() for word in file.readlines()]

    # Generate explanations for the words
    data = generate_explanations(words)

    # Create Excel spreadsheet
    create_excel_sheet(data)

if __name__ == "__main__":
    main()
