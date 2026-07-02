import cv2
import numpy as np
import os

img = cv2.imread("/Users/ayushgupta/Desktop/PYTHON/OPENCV/book.png")

retval , threshold = cv2.threshold(img , 6 , 220 , cv2.THRESH_BINARY_INV)

grayscaled = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
retval2 , threshold2 = cv2.threshold(grayscaled , 12, 255 , cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(grayscaled , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY , 115 , 1)

# ──────────────────────────────────────────────
#  AUTO SAVE — saves all processed images automatically
# ──────────────────────────────────────────────
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)  # Creates 'output/' folder if it doesn't exist

cv2.imwrite(f"{output_dir}/threshold.jpg", threshold)
cv2.imwrite(f"{output_dir}/threshold2.jpg", threshold2)
cv2.imwrite(f"{output_dir}/gaus.jpg", gaus)

print(f"✅ All images saved to '{output_dir}/' folder!")

# ──────────────────────────────────────────────
#  DISPLAY — show all windows
# ──────────────────────────────────────────────
cv2.imshow("Original"  , img)
cv2.imshow("Thresholded" , threshold)
cv2.imshow("Thresholded2" , threshold2)
cv2.imshow("gaus" , gaus)

cv2.waitKey(0)
cv2.destroyAllWindows()
