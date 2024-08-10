import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from variables import *

import os
import csv
import requests
from urllib.parse import urlparse
import pandas as pd

def download_image(url, filename):
    if pd.isna(url) or url == '':
        print(f"Skipping download for {filename} due to missing URL")
        return ''
    try:
        response = requests.get(url)
        response.raise_for_status()
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'wb') as file:
            file.write(response.content)
        return filename
    except requests.RequestException as e:
        print(f"Error downloading image: {e}")
        return ''

def process_csv_and_download_images():
    try:
        df = pd.read_csv(CSV_FILE_PATH, encoding='utf-8')
        for index, row in df.iterrows():
            word = row.iloc[0]  # Use iloc instead of positional indexing
            front_image_url = row.iloc[5]
            back_image_url = row.iloc[6]
            
            front_image_path = download_image(front_image_url, f'./files/images/{word}_front.jpg')
            back_image_path = download_image(back_image_url, f'./files/images/{word}_back.jpg')
            
            df.at[index, 'front_image_path'] = front_image_path
            df.at[index, 'back_image_path'] = back_image_path
        
        df.to_csv(CSV_FILE_PATH_WITH_IMAGES, index=False, encoding='utf-8')
        print(f"Images downloaded and CSV updated. New CSV file: {CSV_FILE_PATH_WITH_IMAGES}")
    except Exception as e:
        print(f"Error processing CSV and downloading images: {e}")
        raise  # Re-raise the exception for better error reporting

if __name__ == "__main__":
    process_csv_and_download_images()