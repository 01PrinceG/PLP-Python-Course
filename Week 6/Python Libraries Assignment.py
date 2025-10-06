import os
import requests
from urllib.parse import urlparse
import uuid

def fetch_image():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Prompt user for image URL
    url = input("Please enter the image URL: ")

    # Create directory if it doesn't exist
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)

    try:
        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for HTTP issues

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename, generate a unique one
        if not filename:
            filename = f"image_{uuid.uuid4().hex}.jpg"

        # Save image
        filepath = os.path.join(folder, filename)
        with open(filepath, "wb") as file:
            file.write(response.content)

        
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}\n")
        print("Connection strengthened. Community enriched.")

    except requests.exceptions.MissingSchema:
        print("Error: Invalid URL format. Please enter a valid URL.")
    except requests.exceptions.ConnectionError:
        print("Error: Connection failed. Check your internet.")
    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except Exception as e:
        print(f" Unexpected Error: {e}")

# Run the function
if __name__ == "__main__":
    fetch_image()

