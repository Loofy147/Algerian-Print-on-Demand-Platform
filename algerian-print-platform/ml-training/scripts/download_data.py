# Algerian Print-on-Demand Platform: Dataset Collection Script
#
# Phase 1, Week 1: Dataset Collection
#
# GOAL: Collect a large and diverse dataset of images suitable for fine-tuning
# an AI image generation model for the Algerian market.
#
# TARGET: 10,000+ images

import os
import requests
import time

# --- CONFIGURATION ---
BASE_OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'datasets', 'raw')
CATEGORIES = {
    "geometric": "Islamic geometric patterns",
    "calligraphy": "Arabic calligraphy",
    # Add other categories here
}
WIKIMEDIA_API_URL = "https://commons.wikimedia.org/w/api.php"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def download_image(url, destination_path, retries=3, backoff_factor=0.5):
    """
    Downloads an image from a URL with retry logic.
    """
    for i in range(retries):
        try:
            response = requests.get(url, stream=True, timeout=15, headers=HEADERS)
            response.raise_for_status()
            with open(destination_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {url}: {e}. Retrying in {backoff_factor * (2 ** i)} seconds...")
            time.sleep(backoff_factor * (2 ** i))
    return False

def fetch_wikimedia_image_urls(search_query, limit=50):
    """
    Fetches image URLs from Wikimedia Commons using a search query.
    """
    print(f"Fetching up to {limit} image URLs for query: '{search_query}'...")
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": search_query,
        "srnamespace": "6",
        "srlimit": limit,
    }
    try:
        response = requests.get(WIKIMEDIA_API_URL, params=params, headers=HEADERS)
        response.raise_for_status()
        data = response.json()

        pages = data.get("query", {}).get("search", [])
        if not pages:
            print("No images found for this search query.")
            return []

        title_string = "|".join([page['title'] for page in pages])

        params_for_urls = {
            "action": "query",
            "format": "json",
            "prop": "imageinfo",
            "iiprop": "url",
            "titles": title_string
        }

        response_urls = requests.get(WIKIMEDIA_API_URL, params=params_for_urls, headers=HEADERS)
        response_urls.raise_for_status()
        url_data = response_urls.json()

        urls = []
        image_pages = url_data.get("query", {}).get("pages", {})
        for page_id in image_pages:
            page = image_pages[page_id]
            if "imageinfo" in page:
                urls.append(page["imageinfo"][0]["url"])

        print(f"Successfully fetched {len(urls)} URLs.")
        return urls

    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return []


def main():
    """
    Main function to run the dataset collection process.
    """
    print("Starting dataset collection...")

    category_key = "geometric"
    search_query = CATEGORIES[category_key]

    output_dir = os.path.join(BASE_OUTPUT_DIR, category_key)
    os.makedirs(output_dir, exist_ok=True)

    image_urls = fetch_wikimedia_image_urls(search_query, limit=20)

    if not image_urls:
        print("No image URLs fetched. Exiting.")
        return

    print(f"\nDownloading a test batch of {len(image_urls)} images to '{output_dir}'...")

    success_count = 0
    for i, url in enumerate(image_urls):
        filename = os.path.basename(url)
        destination = os.path.join(output_dir, filename)

        if download_image(url, destination):
            success_count += 1

        time.sleep(1.5)

    print(f"\nDataset collection complete. Successfully downloaded {success_count}/{len(image_urls)} images.")

if __name__ == "__main__":
    main()
