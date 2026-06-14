import cv2
import numpy as np


def split_image(img):
    h, w = img.shape[:2]

    return (
        img[:h//2, :w//2],
        img[:h//2, w//2:],
        img[h//2:, :w//2],
        img[h//2:, w//2:]
    )


def grayscale(img):
    gray = (
        0.299 * img[:, :, 2] +
        0.587 * img[:, :, 1] +
        0.114 * img[:, :, 0]
    )
    return gray.astype(np.uint8)


def adjust_brightness(img, value):
    bright = img.astype(np.int16) + value
    return np.clip(bright, 0, 255).astype(np.uint8)


def adjust_contrast(img, factor):
    contrast = img.astype(np.float32) * factor
    return np.clip(contrast, 0, 255).astype(np.uint8)


def invert(img):
    return 255 - img


def blur(img, ksize=(5, 5)):
    return cv2.blur(img, ksize)


def sharpen(img):
    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])
    return cv2.filter2D(img, -1, kernel)


def edge_detection(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    edges = cv2.magnitude(sobel_x, sobel_y)

    return np.uint8(np.clip(edges, 0, 255))