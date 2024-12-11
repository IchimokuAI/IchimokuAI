import os

def validate_image(file_path):
    """Validate the uploaded image file format and size."""
    allowed_extensions = ['jpg', 'jpeg', 'png']
    file_extension = file_path.split('.')[-1].lower()
    
    if file_extension not in allowed_extensions:
        raise ValueError(f"Unsupported file type: {file_extension}")
    
    if os.path.getsize(file_path) > 5 * 1024 * 1024:  # 5 MB limit
        raise ValueError("File size exceeds the maximum limit of 5 MB")
    
    return True
