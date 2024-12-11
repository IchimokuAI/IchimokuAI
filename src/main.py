# Main entry point for EudoxAI
if __name__ == "__main__":
    print("Welcome to EudoxAI!")

from nasa_api import fetch_nasa_image

image_path = fetch_nasa_image()
print(f"Downloaded image path: {image_path}")

# src/main.py

from input_handler import validate_image
from image_processor import process_image
from data_interpreter import interpret_data
from twitter_bot import post_to_twitter
from nasa_api import fetch_nasa_image

def main():
    # Fetch the latest NASA image
    image_path = fetch_nasa_image()

    if not image_path:
        print("Failed to fetch a NASA image. Exiting...")
        return

    try:
        # Validate the image
        if validate_image(image_path):
            print("Image validation successful.")

            # Process the image
            telemetry_data = process_image(image_path)
            print("Image processing complete.")

            # Interpret the data
            interpreted_text = interpret_data(telemetry_data)
            print("Data interpretation complete.")

            # Post to Twitter
            post_to_twitter(interpreted_text, image_path)
            print("Data successfully posted to Twitter!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

