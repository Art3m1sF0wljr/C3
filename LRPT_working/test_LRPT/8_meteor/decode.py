import numpy as np
import cv2
import struct

def decode_image(input_binary_path, output_image_path):
    with open(input_binary_path, 'rb') as f:
        # Read the file content
        data = f.read()
    
    custom_string = b'11100001010110101110100010010011'
    access_code = struct.pack('H', 0xAAAA)
    coordinate_flag = struct.pack('H', 0xBBBB)
    
    # Find the custom string to start reading
    start_index = data.find(custom_string)
    if start_index == -1:
        raise ValueError("Custom string not found in the data!")
    
    # Initialize arrays for Magenta, Yellow, Cyan channels
    magenta = np.zeros((512, 512), dtype=np.uint8)
    yellow = np.zeros((512, 512), dtype=np.uint8)
    cyan = np.zeros((512, 512), dtype=np.uint8)
    
    # Process the data
    i = start_index + len(custom_string)
    while i < len(data):
        if data[i:i+len(custom_string)] == custom_string:
            break
        
        # Read the pixel values
        mag, yel, cya = struct.unpack('BBB', data[i:i+3])
        i += 3
        
        # Verify access code
        if data[i:i+len(access_code)] != access_code:
            raise ValueError("Access code not found where expected!")
        i += len(access_code)
        
        # Read the coordinates
        row, col = struct.unpack('HH', data[i:i+4])
        i += 4
        
        # Verify coordinate flag
        if data[i:i+len(coordinate_flag)] != coordinate_flag:
            raise ValueError("Coordinate flag not found where expected!")
        i += len(coordinate_flag)
        
        # Assign values to the channels
        magenta[row, col] = mag
        yellow[row, col] = yel
        cyan[row, col] = cya
    
    # Convert back to BGR
    red = 255 - cyan
    green = 255 - magenta
    blue = 255 - yellow
    reconstructed_image = cv2.merge([blue, green, red])
    
    # Save the reconstructed image
    cv2.imwrite(output_image_path, reconstructed_image)

# Usage
decode_image('rx_data.bin', 'reconstructed_image.jpg')

