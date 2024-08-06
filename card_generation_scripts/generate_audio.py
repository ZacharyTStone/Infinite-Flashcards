import os
import csv
from gtts import gTTS

def generate_audio(text, filename, language="ja"):
    tts = gTTS(text=text, lang=language)
    audio_file = f"./files/{filename}.mp3"
    tts.save(audio_file)
    return audio_file

def main():
    # Specify the path for the CSV files
    csv_file = "./files/Japanese_Word_Examples.csv"
    updated_csv_file = "./files/Japanese_Word_Examples_With_Audio.csv"

    # Read words from the CSV file
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row
        words = [row for row in reader]

    # Generate audio files for each word and example sentence, and add paths
    for row in words:
        word = row[0]
        example_sentence_1 = row[2]
        dictionary_definition = row[4]
        
        # Generate audio files for word, example sentence, and definition
        word_audio_file = generate_audio(word, word)
        example_sentence_1_audio_file = generate_audio(example_sentence_1, f"{word}_example_1")
        dictionary_definition_audio_file = generate_audio(dictionary_definition, f"{word}_definition")
        
        # Add audio file references to the row
        row.append(f"[sound:{word}.mp3]")
        row.append(f"[sound:{word}_example_1.mp3]")
        row.append(f"[sound:{word}_definition.mp3]")

    # Write to a new CSV file
    with open(updated_csv_file, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header + ["Word_Audio", "Example_Sentence_1_Audio", "Dictionary_Definition_Audio"])
        writer.writerows(words)

    print("Audio files have been successfully generated and the CSV file has been updated.")

if __name__ == "__main__":
    main()