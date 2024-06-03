import numpy as np
from scipy.fftpack import ifft2
import struct
import cv2

def decode_image(input_binary_path, output_image_path):
    with open(input_binary_path, 'rb') as f:
        # Read dimensions of the image
        height, width = struct.unpack('II', f.read(8))
        
        # Initialize arrays for magnitude and phase
        magnitude_flat = np.zeros(height * width, dtype=np.uint16)
        phase_flat = np.zeros(height * width, dtype=np.uint16)
        
        # Read magnitude and phase data
        for i in range(height * width):
            magnitude_flat[i], phase_flat[i] = struct.unpack('HH', f.read(4))
        
        # Reshape the arrays
        magnitude = magnitude_flat.reshape((height, width))
        phase = phase_flat.reshape((height, width))
        
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
decode_image('rx_data.bin.truncated', 'reconstructed_image.png')

