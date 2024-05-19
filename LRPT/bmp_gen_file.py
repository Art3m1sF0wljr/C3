import binascii
import math
from PIL import Image

def hex_to_rgb(hex_str):
    """Convert hex string to RGB tuple."""
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

def create_bitmap(hex_file_path):
    try:
        with open(hex_file_path, 'rb') as file:  # Open file in binary mode
            hex_data = file.read()

        # Group hex data into triplets
        triplets = [hex_data[i:i+6] for i in range(0, len(hex_data), 6)]

        # Convert triplets to RGB tuples
        pixels = [hex_to_rgb(binascii.hexlify(triplet).decode()) for triplet in triplets]

        # Determine dimensions of the bitmap
        num_pixels = len(pixels)
        num_rows = math.ceil(num_pixels / 456)
        num_cols = min(num_pixels, 456)

        # Create image
        bitmap = Image.new('RGB', (num_cols, num_rows))

        # Populate image with pixels
        for row in range(num_rows):
            for col in range(num_cols):
                if (row * 456 + col) < num_pixels:
                    bitmap.putpixel((col, row), pixels[row * 456 + col])
                else:
                    # Color remaining pixels green
                    bitmap.putpixel((col, row), (0, 255, 0))

        return bitmap

    except FileNotFoundError:
        print("File not found.")

def save_bitmap(bitmap, file_path):
    try:
        bitmap.save(file_path, "BMP")
        print("Bitmap saved successfully.")
    except Exception as e:
        print(f"Error occurred while saving bitmap: {e}")

# Example usage:
input_file = "test_13_LRPT.txt"
output_file = "output.bmp"

bitmap = create_bitmap(input_file)
if bitmap:
    save_bitmap(bitmap, output_file)
