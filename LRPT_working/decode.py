import numpy as np
import cv2
import struct

def decode_image(input_binary_path, output_image_path):
    with open(input_binary_path, 'rb') as f:
        # Read the file content
        data = f.read()
    
    access_code = struct.pack('H', 0xAAAA)
    coordinate_flag = struct.pack('H', 0xBBBB)
    
    # Initialize arrays for Magenta, Yellow, Cyan channels
    magenta = np.zeros((512, 512), dtype=np.uint8)
    yellow = np.zeros((512, 512), dtype=np.uint8)
    cyan = np.zeros((512, 512), dtype=np.uint8)
    
    # Initialize index for reading data
    i = 0
    data_length = len(data)
    
    while i < data_length:
        # Look for access code
        ac_index = data.find(access_code, i)
        if ac_index == -1:
            break  # No more access codes found
        
        # Read pixel values before the access code
        if ac_index >= 3:
            try:
                mag, yel, cya = struct.unpack('BBB', data[ac_index-3:ac_index])
                # Validate color values
                if not (0 <= mag <= 255 and 0 <= yel <= 255 and 0 <= cya <= 255):
                    raise ValueError("Color value out of range")
            except (struct.error, ValueError):
                i = ac_index + len(access_code)
                continue
        
        # Move index to after the access code
        i = ac_index + len(access_code)
        
        # Look for coordinate flag
        cf_index = data.find(coordinate_flag, i)
        if cf_index == -1:
            break  # No more coordinate flags found
        
        # Read coordinates before the coordinate flag
        if cf_index >= 4:
            try:
                row, col = struct.unpack('HH', data[cf_index-4:cf_index])
                # Validate coordinates
                if not (0 <= row < 512 and 0 <= col < 512):
                    raise ValueError("Coordinate out of range")
            except (struct.error, ValueError):
                i = cf_index + len(coordinate_flag)
                continue
        
        # Assign values to the channels only if coordinates and pixel values are valid
        try:
            magenta[row, col] = mag
            yellow[row, col] = yel
            cyan[row, col] = cya
        except (NameError, ValueError):
            # Skip assignment if pixel values are invalid
            pass
        
        # Move index to after the coordinate flag
        i = cf_index + len(coordinate_flag)
    
    # Convert back to BGR
    red = 255 - cyan
    green = 255 - magenta
    blue = 255 - yellow
    reconstructed_image = cv2.merge([blue, green, red])
    
    # Save the reconstructed image
    cv2.imwrite(output_image_path, reconstructed_image)

# Usage
decode_image('rx_data.bin', 'reconstructed_image.jpg')

