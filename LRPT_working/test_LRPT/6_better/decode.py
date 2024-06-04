import numpy as np
from scipy.fftpack import ifft2
import struct
import cv2

def decode_image(input_binary_path, output_image_path, flag_length=1024, access_code_interval=1024):
    with open(input_binary_path, 'rb') as f:
        # Read the file content
        data = f.read()
        
        # Custom string and subset length
        custom_string = b'11100001010110101110100010010011'
        subset_length = 6
        
        # Find the second instance of any subset of the custom string
        first_index = -1
        second_index = -1
        for i in range(len(custom_string) - subset_length + 1):
            subset = custom_string[i:i + subset_length]
            if first_index == -1:
                first_index = data.find(subset)
            else:
                second_index = data.find(subset, first_index + len(subset))
                if second_index != -1:
                    break
        
        if first_index == -1 or second_index == -1:
            raise ValueError("Second instance of the custom string subset not found!")
        
        # Adjust start index to end of the second custom string
        start_index = second_index + len(custom_string)
        
        # Find the access code "aa aa" (0xAAAA) after the start index
        access_code = struct.pack('H', 0xAAAA)
        start_index = data.find(access_code, start_index)
        if start_index == -1:
            raise ValueError("Access code not found after the custom string!")
        
        # Adjust start index to the beginning of the data
        start_index += len(access_code)
        
        # Initialize arrays for magnitude and phase
        num_elements = 256 * 256
        magnitude_flat = np.zeros(num_elements, dtype=np.uint16)
        phase_flat = np.zeros(num_elements, dtype=np.uint16)
        
        # Read magnitude and phase data with access code
        i = start_index
        j = 0
        while i < len(data) and j < num_elements:
            if data[i:i+2] == access_code:
                i += 2  # skip access code
                continue
            try:
                mag, phs = struct.unpack('HH', data[i:i+4])
            except struct.error:
                break  # if not enough bytes to unpack, stop
            magnitude_flat[j] = mag
            phase_flat[j] = phs
            i += 4
            j += 1
        
        # Reshape the arrays
        magnitude = magnitude_flat.reshape((256, 256))
        phase = phase_flat.reshape((256, 256))
        
        # Dequantize the data
        dequantized_magnitude = magnitude.astype(np.float32)
        dequantized_phase = (phase.astype(np.float32) / 65535) * (2 * np.pi) - np.pi
        
        # Combine magnitude and phase to complex form
        f_transform = dequantized_magnitude * np.exp(1j * dequantized_phase)
        
        # Perform inverse FFT
        reconstructed_image = np.abs(ifft2(f_transform))
        
        # Normalize image to 8-bit range
        reconstructed_image = np.uint8(255 * (reconstructed_image / np.max(reconstructed_image)))
        
        # Save the reconstructed image
        cv2.imwrite(output_image_path, reconstructed_image)

# Usage
decode_image('rx_data.bin', 'reconstructed_image.jpg')

