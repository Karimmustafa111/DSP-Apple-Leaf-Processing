import cv2
import os
import numpy as np

input_folder = r"E:\DSP\archive (2)\Apple DS\Apple_HE"
output_folder = "Apple_HE_Processed"
os.makedirs(output_folder, exist_ok=True)

for img_name in os.listdir(input_folder):
    img_path = os.path.join(input_folder, img_name)
    img = cv2.imread(img_path)
    
    if img is not None:
        img = cv2.resize(img, (256, 256))
        
        # Simulate Periodic Noise 
        row, col, ch = img.shape
        for i in range(0, row, 10):
            img[i:i+2, :] = img[i:i+2, :] + 50 # horizontal lines
        img_periodic = np.clip(img, 0, 255).astype(np.uint8)
        
        # Clear Periodic noise using Blur trick
        smoothed = cv2.blur(img_periodic, (3, 3))
        
        # Convert to Gray Image
        gray_img = cv2.cvtColor(smoothed, cv2.COLOR_BGR2GRAY)
        
        # Convert to Binary Image
        _, binary_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
        
        # Convert Back to 3 Channels
        final_img = cv2.cvtColor(binary_img, cv2.COLOR_GRAY2BGR)
        
        cv2.imwrite(os.path.join(output_folder, img_name), final_img)

print("✅ Apple_HE file done: Periodic Noise + Gray + Binary.")