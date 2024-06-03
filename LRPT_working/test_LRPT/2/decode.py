import numpy as np
from scipy.fftpack import ifft2
import struct
import cv2

def decode_image(input_binary_path, output_image_path, flag_length=30):
    with open(input_binary_path, 'rb') as f:
        # Read the file content
        data = f.read()
        
        # Find the start flag (250 zero bytes)
        zero_flag = b'\x00' * flag_length
        start_index = data.find(zero_flag)
        if start_index == -1:
            raise ValueError("Start flag not found!")
        
        # Skip to the end of the zero flag
        while start_index < len(data) and data[start_index] == 0:
            start_index += 1
        
        # The actual data starts after the flag
        data = data[start_index:]
        
        # Initialize arrays for magnitude and phase
        num_elements = 512 * 512
        magnitude_flat = np.zeros(num_elements, dtype=np.uint16)
        phase_flat = np.zeros(num_elements, dtype=np.uint16)
        
        # Read magnitude and phase data
        for i in range(num_elements):
            mag, phs = struct.unpack('HH', data[i*4:i*4+4])
            magnitude_flat[i] = mag
            phase_flat[i] = phs
        
        # Reshape the arrays
        magnitude = magnitude_flat.reshape((512, 512))
        phase = phase_flat.reshape((512, 512))
        
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

