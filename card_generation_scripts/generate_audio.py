import os
import csv
from gtts import gTTS

def generate_audio(text, filename, language="ja"):
    tts = gTTS(text=text, lang=language)
    audio_file = f"./files/{filename}.mp3"
    tts.save(audio_file)
    return audio_file

def main():
    # CSVファイルのパスを指定
    csv_file = "./files/Japanese_Word_Examples.csv"
    updated_csv_file = "./files/Japanese_Word_Examples_With_Audio.csv"

    # CSVファイルから単語を読み込む
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        header = next(reader)  # ヘッダー行をスキップ
        words = [row for row in reader]

    # 各単語と例文のオーディオファイルを生成し、パスを追加
    for row in words:
        word = row[0]
        example_sentence_1 = row[2]
        
        word_audio_file = generate_audio(word, word)
        example_sentence_1_audio_file = generate_audio(example_sentence_1, f"{word}_example_1")
        
        row.append(f"[sound:{word}.mp3]")
        row.append(f"[sound:{word}_example_1.mp3]")

    # 新しいCSVファイルに書き込む
    with open(updated_csv_file, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header + ["Word_Audio", "Example_Sentence_1_Audio"])
        writer.writerows(words)

    print("オーディオファイルが正常に生成され、CSVファイルが更新されました。")

if __name__ == "__main__":
    main()
