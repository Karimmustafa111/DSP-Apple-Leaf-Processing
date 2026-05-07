import cv2
import os
import numpy as np
from PIL import Image

input_folder = r"E:\DSP\archive (2)\Apple DS\Apple_BR"
output_folder = "Apple_BR_Processed"
os.makedirs(output_folder, exist_ok=True)

for img_name in os.listdir(input_folder):
    img_path = os.path.join(input_folder, img_name)
    
    # Read image
    pil_img = Image.open(img_path)
    
    # Geometric Transformations
    pil_img = pil_img.resize((300, 300)) # Resize
    pil_img = pil_img.crop((20, 20, 280, 280)) # Crop
    pil_img = pil_img.rotate(45) # Rotate
    pil_img = pil_img.transpose(Image.FLIP_LEFT_RIGHT) # Flip
    
    # Convert image from PIL to CV2
    img_cv2 = np.array(pil_img)
    img_cv2 = cv2.cvtColor(img_cv2, cv2.COLOR_RGB2BGR) # Fix color to BGR
    img_cv2 = cv2.resize(img_cv2, (256, 256)) # For merging
    
    # Add Salt and Pepper Noise
    noise = np.zeros(img_cv2.shape, np.uint8)
    cv2.randu(noise, 0, 255)
    salt_pepper = img_cv2.copy()
    salt_pepper[noise < 10] = 0     # Pepper
    salt_pepper[noise > 245] = 255  # Salt 
    
    # Clean the image
    cleaned_img = cv2.medianBlur(salt_pepper, 5)
    
    cv2.imwrite(os.path.join(output_folder, img_name), cleaned_img)

print("✅ Apple_BR file done: PIL + Geometry + Salt & Papper.")