import numpy as np
import cv2
from scipy.fftpack import fft2
import struct
import os

def encode_image(image_path, output_binary_path, access_code_interval=1024):
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
    
    # Create random garbage data, start flag, and end flag
    garbage_data = os.urandom(4096)
    start_flag = b'\xDD' * 1024
    end_flag = b'\xFF' * 1024
    access_code = struct.pack('H', 0xAAAA)
    custom_string = b'11100001010110101110100010010011'
    
    # Pack data into binary format
    with open(output_binary_path, 'wb') as f:
        # Write garbage data
        f.write(garbage_data)
        
        # Write custom string
        f.write(custom_string)
        
        # Write start flag
        f.write(start_flag)
        
        # Write custom string again
        f.write(custom_string)
        
        # Write magnitude and phase data with access code
        for i, (mag, phs) in enumerate(zip(magnitude_flat, phase_flat)):
            if i % (access_code_interval // 4) == 0:
                f.write(access_code)
            f.write(struct.pack('HH', mag, phs))
        
        # Write end flag
        f.write(custom_string)
        f.write(end_flag)
        f.write(custom_string)
        f.write(garbage_data)

# Usage
encode_image('asd.png', 'tx_data.bin')

