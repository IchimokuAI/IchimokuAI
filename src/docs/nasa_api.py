# src/nasa_api.py

import requests
import os

# NASA API key 
NASA_API_KEY = "X2Z9Y3T8Q6B1N0R5L4K7P8M1W9V2A6C3"

def fetch_nasa_image(save_directory="data/"):
    """
    Fetches the latest NASA image from the Astronomy Picture of the Day API.
    Saves the image to the specified directory.
    """
    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
    
    try:
        print("Fetching the latest NASA telemetry photo...")
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        image_url = data.get("url")
        image_title = data.get("title", "nasa_image").replace(" ", "_")
        
        if not image_url:
            raise ValueError("No image URL found in API response.")
        
        # Download the image
        img_response = requests.get(image_url, stream=True)
        img_response.raise_for_status()
        
        # Ensure the save directory exists
        os.makedirs(save_directory, exist_ok=True)
        image_file_path = os.path.join(save_directory, f"{image_title}.jpg")
        
        with open(image_file_path, "wb") as file:
            for chunk in img_response.iter_content(1024):
                file.write(chunk)
        
        print(f"Image saved successfully: {image_file_path}")
        return image_file_path
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching NASA image: {e}")
        return None
