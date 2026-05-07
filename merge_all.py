import cv2
import os

base_path = r"E:\DSP\archive (2)\Apple DS"
folders = ["Apple_BR", "Apple_CR", "Apple_HE"]

for folder in folders:
    # The Original Folder
    orig_folder = os.path.join(base_path, folder)
    
    proc_folder = f"{folder}_Processed"
    final_folder = f"{folder}_Final_Merged"
    
    # Create final merge folder
    os.makedirs(final_folder, exist_ok=True)
    
    for img_name in os.listdir(orig_folder):
        orig_img_path = os.path.join(orig_folder, img_name)
        proc_img_path = os.path.join(proc_folder, img_name)
        
        if os.path.exists(proc_img_path):
            orig_img = cv2.imread(orig_img_path)
            proc_img = cv2.imread(proc_img_path)
            
            if orig_img is not None and proc_img is not None:
                
                orig_img = cv2.resize(orig_img, (256, 256))
                
                # Merge horizontally
                merged_img = cv2.hconcat([orig_img, proc_img])
                
                # Save Merged Image
                cv2.imwrite(os.path.join(final_folder, img_name), merged_img)

print("All original images merged successfully 🎉")