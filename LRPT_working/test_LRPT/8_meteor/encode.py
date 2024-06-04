import numpy as np
import cv2
import struct
import os

def encode_image(image_path, output_binary_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Resize image to 512x512 if necessary
    image = cv2.resize(image, (512, 512))
    
    # Split the image into Magenta, Yellow, Cyan channels
    blue, green, red = cv2.split(image)
    magenta = 255 - green
    yellow = 255 - blue
    cyan = 255 - red
    
    # Flatten the channels
    magenta_flat = magenta.flatten()
    yellow_flat = yellow.flatten()
    cyan_flat = cyan.flatten()
    
    # Create the flags and custom string
    custom_string = b'11100001010110101110100010010011'
    access_code = struct.pack('H', 0xAAAA)
    coordinate_flag = struct.pack('H', 0xBBBB)
    
    # Pack data into binary format
    with open(output_binary_path, 'wb') as f:
        # Write custom string
        f.write(custom_string)
        
        # Write pixel values, coordinates, and flags
        for idx in range(len(magenta_flat)):
            row, col = divmod(idx, 512)
            f.write(struct.pack('BBB', magenta_flat[idx], yellow_flat[idx], cyan_flat[idx]))
            f.write(access_code)
            f.write(struct.pack('HH', row, col))
            f.write(coordinate_flag)
        
        # Write custom string again to indicate the end
        f.write(custom_string)

# Usage
encode_image('asd.png', 'tx_data.bin')

