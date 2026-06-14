Image Processing Project (NumPy + OpenCV)

// Overview 

This project is about basic image processing techniques using python. it treats images as Numpy arrays and performs operations like splitting, cropping, and transformations.

//tech

Pyhton
Numpy
Opencv

// Features 

Phase 1 : basic_slicing
Load images
Understand image shape (height, width, channels)
Split image into quadrants
Extract left and right halves
Crop specific regions

Phase 2: Grayscale Conversion

Manual grayscale conversion using NumPy
OpenCV grayscale conversion comparison
Understanding color channels (BGR)

Phase 3: Brightness Adjustment

Increase image brightness
Understand pixel intensity values
Handle overflow using clipping
Practice array-wide transformations

Phase 4: Contrast Adjustment

Increase and decrease image contrast
Understand pixel scaling
Use clipping to maintain valid pixel values
Practice vectorized operations

Phase 5-6: Blur and Sharpen

Apply averaging blur using a 5×5 kernel
Learn neighborhood-based image processing
Apply sharpening using a custom kernel
Understand how kernels affect image details

Phase 7: Edge Detection

Detect edges using Sobel filters
Understand image gradients (X and Y direction)
Combine gradients to extract structure
Learn foundation of feature detection in computer vision


// Concepts Learned
NumPy slicing
Array indexing
Image representation as matrices
Basic computer vision workflow

// How to Run
```bash
pip install -r requirements.txt
python src/phase1_basic_slicing.py