# DSP-Apple-Leaf-Processing

# DSP Apple Leaf Image Processing 🍏

This project applies various Digital Signal Processing (DSP) and Image Processing techniques to an Apple Leaf dataset. It was developed by a team of 5 students.

## 🛠️ Techniques Used:
1. **Geometric Transformations:** Resize, Crop, Rotate, Flip (using PIL).
2. **Color Spaces:** RGB, BGR, HSV, Grayscale, Binary Image.
3. **Noise Simulation & Removal:**
   - Salt and Pepper Noise (Cleaned with Median Filter).
   - Gaussian Noise (Cleaned with Gaussian Blur).
   - Periodic Noise (Cleaned with Blur filter).
4. **Edge Detection:** Canny Edge Detection.
5. **Image Segmentation:** Thresholding.

## 📁 Files Description:
- `process_BR.py`: Applies geometric transformations, adds Salt & Pepper noise, and removes it.
- `process_CR.py`: Manipulates HSV color space, adds and removes Gaussian Noise.
- `process_HE.py`: Simulates Periodic Noise, converts to Grayscale and Binary.
- `merge_all.py`: Automatically merges the original and processed images side-by-side for comparison.
