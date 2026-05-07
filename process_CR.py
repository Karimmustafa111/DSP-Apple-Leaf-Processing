import cv2
import os
import numpy as np

input_folder = r"E:\DSP\archive (2)\Apple DS\Apple_CR"
output_folder = "Apple_CR_Processed"
os.makedirs(output_folder, exist_ok=True)

for img_name in os.listdir(input_folder):
    img_path = os.path.join(input_folder, img_name)
    img = cv2.imread(img_path)
    
    if img is not None:
        img = cv2.resize(img, (256, 256))
        
        # Color Spaces
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # RGB
        img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV) # HSV
        
        # Increase brightness (value channel)
        img_hsv[:, :, 2] = np.clip(img_hsv[:, :, 2] * 1.2, 0, 255) 
        
        # Convert to BGR for Processing and Saving
        img_bgr_modified = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
        
        # Add Gaussian Noise
        row, col, ch = img_bgr_modified.shape
        gauss = np.random.normal(0, 25, (row, col, ch)) # Generate noise
        noisy_img = img_bgr_modified + gauss
        noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)
        
        # Clean the Gaussian Noise
        cleaned_img = cv2.GaussianBlur(noisy_img, (5, 5), 0)
        
        cv2.imwrite(os.path.join(output_folder, img_name), cleaned_img)

print("✅ Apple_CR file done: Color Spaces + Gaussian Noise.")