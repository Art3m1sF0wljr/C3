import numpy as np
import cv2
from scipy.fftpack import fft2
import struct

def encode_image(image_path, output_binary_path):
    # Load image and convert to grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Resize image to 512x512 if necessary
    image = cv2.resize(image, (512, 512))
    
    # Perform FFT
    f_transform = fft2(image)
    magnitude = np.abs(f_transform)
    phase = np.angle(f_transform)
    
    # Quantize magnitude and phase (simple example)
    quantized_magnitude = np.round(magnitude).astype(np.uint16)
    quantized_phase = np.round((phase + np.pi) / (2 * np.pi) * 65535).astype(np.uint16)  # scale to 0-65535
    
    # Flatten the arrays for transmission
    magnitude_flat = quantized_magnitude.flatten()
    phase_flat = quantized_phase.flatten()
    
    # Create start flag
    start_flag = b'\x00' * 1024
    
    # Pack data into binary format
    with open(output_binary_path, 'wb') as f:
        # Write start flag
        f.write(start_flag)
        
        # Write magnitude and phase data
        for mag, phs in zip(magnitude_flat, phase_flat):
            f.write(struct.pack('HH', mag, phs))

# Usage
encode_image('asd.png', 'tx_data.bin')

