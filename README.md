#Image Processing Toolkit (NumPy + OpenCV)

A mini image processing library built from scratch to understand how images are manipulated using arrays.



#Overview

This project demonstrates how images are not “magic files” but simple NumPy arrays that can be transformed using mathematical operations.

It starts from basic slicing and progresses to classical computer vision filters like blur, sharpen, and edge detection.



#What I Learned

How images are represented as NumPy arrays (H × W × C)
Pixel-level manipulation using slicing
Grayscale conversion from RGB/BGR channels
Brightness and contrast transformations
Kernel-based filtering (blur & sharpen)
Edge detection using Sobel filters



#Features

Image splitting into quadrants
Grayscale conversion
Brightness adjustment
Contrast adjustment
Image inversion (negative effect)
Blur filtering
Sharpening filter
Edge detection



#Project Structure

src/
image_processor.py
main.py 

images/
My_photo.jpg 



#How to Run

```bash
pip install -r requirements.txt
python src/main.py