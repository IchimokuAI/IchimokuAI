# src/image_processor.py

import cv2
import numpy as np
import random

def process_image(file_path):
    """
    Simulates telemetry image analysis using OpenCV.
    """
    print(f"Analyzing telemetry data from {file_path}...")

    # Simulate loading the image
    image = cv2.imread(file_path)
    if image is None:
        raise ValueError("Failed to load image. Ensure the file path is correct.")
    
    # Simulate image preprocessing
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    edges = cv2.Canny(blurred_image, 50, 150)

    # Simulate AI-based object detection (fake data)
    detected_objects = ["Mars Rover", "Satellite", "Space Debris"]
    detected_object = random.choice(detected_objects)

    # Simulate random telemetry data extraction
    telemetry_data = {
        "object_detected": detected_object,
        "coordinates": (random.uniform(-180, 180), random.uniform(-90, 90)),
        "radiation_levels": round(random.uniform(0.1, 5.0), 2),
        "temperature": round(random.uniform(-100, 100), 2),
    }

    print("Image analysis complete.")
    return telemetry_data
