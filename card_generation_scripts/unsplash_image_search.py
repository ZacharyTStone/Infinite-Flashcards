import os
from pyunsplash import PyUnsplash
from dotenv import load_dotenv
import requests
from PIL import Image

# Load environment variables
load_dotenv()

# Get Unsplash API key from environment variable
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")

# Initialize PyUnsplash
pu = PyUnsplash(api_key=UNSPLASH_ACCESS_KEY)

def search_and_download_image(query, filename):
    # Search for photos
    photos = pu.photos(type_='random', count=1, featured=True, query=query)
    
    # Get the first photo
    [photo] = photos.entries
    
    # Download the image
    response = requests.get(photo.link_download, allow_redirects=True)
    
    # Save the image
    with open(filename, 'wb') as f:
        f.write(response.content)
    
    print(f"Image downloaded and saved as {filename}")
    
    # Display image info
    print(f"Photo ID: {photo.id}")
    print(f"Photographer: {photo.photographer}")
    print(f"Photo URL: {photo.link_html}")

    # Open and display the image
    Image.open(filename).show()

# Example usage
search_and_download_image("japanese landscape", "unsplash_image.jpg")
