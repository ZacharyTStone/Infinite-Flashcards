import sys
import requests
from variables import UNSPLASH_ACCESS_KEY

def search_image(query, num_results=1):
    url = "https://api.unsplash.com/photos/random"
    headers = {
        "Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"
    }
    params = {
        "query": query,
        "count": num_results,
        "orientation": "landscape"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        results = response.json()

        if isinstance(results, list) and len(results) > 0:
            return [photo['urls']['regular'] for photo in results]
        else:
            print(f"No image results found for query: {query}")
            return []

    except requests.RequestException as e:
        print(f"Error occurred while searching for images: {e}")
        return []

# Test the function
if __name__ == "__main__":
    test_query = "富士山"  # Mount Fuji
    image_urls = search_image(test_query, num_results=2)
    print(f"Image URLs for '{test_query}':")
    for url in image_urls:
        print(url)