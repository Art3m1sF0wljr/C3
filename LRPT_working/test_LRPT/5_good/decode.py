import numpy as np
from scipy.fftpack import ifft2
import struct
import cv2

def decode_image(input_binary_path, output_image_path, access_code_interval=1024):
    with open(input_binary_path, 'rb') as f:
        # Read the file content
        data = f.read()
        
        # Custom string and subset length
        custom_string = b'11100001010110101110100010010011'
        subset_length = 6
        
        # Find the second instance of any subset of the custom string
        def find_nth_instance(data, custom_string, subset_length, n):
            instances = []
            for i in range(len(custom_string) - subset_length + 1):
                subset = custom_string[i:i + subset_length]
                pos = data.find(subset)
                while pos != -1:
                    instances.append(pos)
                    pos = data.find(subset, pos + len(subset))
                    if len(instances) == n:
                        return instances[-1]
            return -1

        first_index = find_nth_instance(data, custom_string, subset_length, 1)
        if first_index == -1:
            raise ValueError("First instance of the custom string subset not found!")
        
        second_index = find_nth_instance(data, custom_string, subset_length, 2)
        if second_index == -1:
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
        
        # Find the third instance of any subset of the custom string
        third_index = find_nth_instance(data[start_index:], custom_string, subset_length, 1)
        if third_index == -1:
            raise ValueError("Third instance of the custom string subset not found!")
        
        # Adjust end index to start of the third custom string
        end_index = start_index + third_index
        
        # The actual data is between the access code and the start of the third custom string
        data = data[start_index:end_index]
        
        # Initialize arrays for magnitude and phase
        num_elements = 512 * 512
        magnitude_flat = np.zeros(num_elements, dtype=np.uint16)
        phase_flat = np.zeros(num_elements, dtype=np.uint16)
        
        # Read magnitude and phase data with access code
        i = 0
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

