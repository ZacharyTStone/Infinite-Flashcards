# Infinite Flashcards

This project is a Python application that automatically generates high-quality Japanese Anki flashcards from a simple word list using OpenAI's language models. It streamlines the process of creating comprehensive study materials for Japanese language learners.

## Features

- **AI-Powered Content Generation**: Uses OpenAI to create accurate and natural-sounding example sentences and definitions
- **Complete Flashcard Information**: Each card includes:
  - Word in Japanese (kanji)
  - Reading in hiragana with NHK standard pitch accent notation
  - Two contextual example sentences
  - English translation/definition
  - Audio pronunciation for the word, examples, and definition
- **Automatic Anki Integration**: Directly imports generated cards into your Anki collection
- **Batch Processing**: Process multiple words at once efficiently

## System Requirements

- Python 3.6+
- Anki desktop application
- AnkiConnect add-on installed in Anki
- Internet connection for OpenAI API and audio generation
- OpenAI API key

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Infinite-Flashcards.git
   cd Infinite-Flashcards
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with your API keys:

   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ANKI_CONNECT_URL=http://localhost:8765
   ANKI_DECK_NAME=Japanese
   ```

4. Ensure you have Anki installed and set up with the AnkiConnect add-on.

## Setup Anki

1. Install [Anki](https://apps.ankiweb.net/) if you haven't already
2. Install the [AnkiConnect add-on](https://ankiweb.net/shared/info/2055492159) in Anki:
   - Open Anki
   - Go to Tools > Add-ons > Get Add-ons
   - Enter the code: `2055492159`
   - Restart Anki

## Usage

1. Add your Japanese words to the `words.txt` file in the `card_generation_scripts` folder:

   - One word per line or space-separated words
   - Example:
     ```
     食べ物
     勉強
     日本語
     ```

2. Make sure Anki is running with the AnkiConnect add-on active

3. Run the main script:

   ```bash
   python main.py
   ```

   When you first run the script, it will create an empty `words.txt` file if one doesn't exist. You can also refer to the `words-EXAMPLE.txt` file for reference.

4. The script will:
   - Generate detailed card content using OpenAI
   - Create audio files for pronunciation
   - Build an Anki package
   - Import the cards into your specified Anki deck

## Project Structure

```
Infinite-Flashcards/
├── .env                       # Environment variables (API keys, etc.)
├── .env_example               # Example environment file
├── .gitignore                 # Git ignore file
├── README.md                  # This documentation file
├── requirements.txt           # Python dependencies
├── main.py                    # Main script to run the application
├── utils.py                   # Utility functions
├── variables.py               # Global variables and configurations
└── card_generation_scripts/   # Directory containing card generation scripts
    ├── generate_csv.py        # Creates CSV with word data from OpenAI
    ├── generate_audio.py      # Generates audio files using gTTS
    ├── make_anki_pkg.py       # Creates Anki package from CSV and audio
    ├── import_to_anki.py      # Imports the package into Anki
    ├── create_text_files.py   # Creates necessary text files
    ├── words-EXAMPLE.txt      # Example word file for reference
    └── words.txt              # Your list of Japanese words to process
```

## Customization

- **Model Selection**: You can modify the OpenAI model in `generate_csv.py` (default is `o1-mini`)
- **Card Format**: Edit the template in `make_anki_pkg.py` to change card appearance
- **Audio Settings**: Adjust settings in `generate_audio.py` for different voices or audio quality. The application uses Google's Text-to-Speech (gTTS) service to generate audio pronunciations.

## Troubleshooting

- **Anki Connection Error**: Ensure Anki is running and AnkiConnect add-on is properly installed
- **API Key Issues**: Verify your OpenAI API key is correct and has sufficient credits
- **File Not Found Errors**: Make sure the `words.txt` file exists and contains words to process
- **Python Environment Issues**: If you encounter dependency errors, try creating a virtual environment before installing requirements

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT

---

# 無限フラッシュカード

このプロジェクトは、OpenAI を使用して日本語の単語リストから Anki フラッシュカードを自動生成する Python アプリケーションです。日本語学習者が質の高い学習教材を簡単に作成できるようにします。

## 特徴

- **AI 駆動コンテンツ生成**: OpenAI を使用して正確で自然な例文と定義を作成
- **完全なフラッシュカード情報**: 各カードには以下が含まれます：
  - 日本語の単語（漢字）
  - ひらがなでの読み方と NHK 標準のピッチアクセント表記
  - 二つの文脈的な例文
  - 英語での翻訳・定義
  - 単語、例文、定義の音声発音
- **Anki 自動連携**: 生成されたカードを直接 Anki コレクションにインポート
- **バッチ処理**: 複数の単語を一度に効率的に処理

## システム要件

- Python 3.6 以上
- Anki デスクトップアプリケーション
- Anki の AnkiConnect アドオン
- OpenAI API とオーディオ生成のためのインターネット接続
- OpenAI API キー

## インストール

1. リポジトリをクローンします：

   ```bash
   git clone https://github.com/yourusername/Infinite-Flashcards.git
   cd Infinite-Flashcards
   ```

2. 必要な依存関係をインストールします：

   ```bash
   pip install -r requirements.txt
   ```

3. ルートディレクトリに`.env`ファイルを作成し、API キーを設定します：

   ```
   OPENAI_API_KEY=あなたのOpenAI_APIキーをここに入力
   ANKI_CONNECT_URL=http://localhost:8765
   ANKI_DECK_NAME=Japanese
   ```

4. Anki がインストールされ、AnkiConnect アドオンで設定されていることを確認します。

## Anki のセットアップ

1. まだインストールしていない場合は [Anki](https://apps.ankiweb.net/) をインストールします
2. Anki に [AnkiConnect アドオン](https://ankiweb.net/shared/info/2055492159) をインストールします：
   - Anki を開く
   - ツール > アドオン > アドオンを取得する に進む
   - コード「2055492159」を入力
   - Anki を再起動

## 使用方法

1. `card_generation_scripts` フォルダ内の `words.txt` ファイルに日本語の単語を追加します：

   - 1 行に 1 単語、またはスペースで区切られた単語
   - 例：
     ```
     食べ物
     勉強
     日本語
     ```

2. AnkiConnect アドオンが有効な状態で Anki が実行されていることを確認します

3. メインスクリプトを実行します：

   ```bash
   python main.py
   ```

   初めてスクリプトを実行する場合、`words.txt` ファイルが存在しなければ空のファイルが作成されます。参考として `words-EXAMPLE.txt` ファイルも確認できます。

4. スクリプトは以下を行います：
   - OpenAI を使用して詳細なカードコンテンツを生成
   - 発音のための音声ファイルを作成
   - Anki パッケージを構築
   - 指定した Anki デッキにカードをインポート

## プロジェクト構造

```
Infinite-Flashcards/
├── .env                       # 環境変数（APIキーなど）
├── .env_example               # 環境ファイルの例
├── .gitignore                 # Gitの無視ファイル
├── README.md                  # このドキュメントファイル
├── requirements.txt           # Python依存関係
├── main.py                    # アプリケーションを実行するメインスクリプト
├── utils.py                   # ユーティリティ関数
├── variables.py               # グローバル変数と設定
└── card_generation_scripts/   # カード生成スクリプトを含むディレクトリ
    ├── generate_csv.py        # OpenAIから単語データを含むCSVを作成
    ├── generate_audio.py      # gTTSを使用して音声ファイルを生成
    ├── make_anki_pkg.py       # CSVとオーディオからAnkiパッケージを作成
    ├── import_to_anki.py      # パッケージをAnkiにインポート
    ├── create_text_files.py   # 必要なテキストファイルを作成
    ├── words-EXAMPLE.txt      # 参考用の単語ファイル例
    └── words.txt              # 処理する日本語単語のリスト
```

## カスタマイズ

- **モデル選択**: `generate_csv.py` で OpenAI モデルを変更できます（デフォルトは `o1-mini`）
- **カードフォーマット**: `make_anki_pkg.py` のテンプレートを編集してカードの外観を変更
- **オーディオ設定**: `generate_audio.py` の設定を調整して、異なる音声や音質を設定。このアプリケーションは Google の Text-to-Speech（gTTS）サービスを使用して音声発音を生成します。

## トラブルシューティング

- **Anki 接続エラー**: Anki が実行中で、AnkiConnect アドオンが適切にインストールされていることを確認
- **API キーの問題**: OpenAI API キーが正しく、十分なクレジットがあることを確認
- **ファイルが見つからないエラー**: `words.txt` ファイルが存在し、処理する単語が含まれていることを確認
- **Python 環境の問題**: 依存関係エラーが発生した場合は、要件をインストールする前に仮想環境を作成してみてください

## 貢献

貢献は大歓迎です！プルリクエストを自由に提出してください。

## ライセンス

MIT
