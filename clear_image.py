"""
🔍 Clear Your Image - Make blurry images readable again!

This script uses OpenCV to enhance blurry/dark images (especially text documents)
by applying Gaussian blur for noise reduction followed by multiple thresholding
techniques to produce crystal-clear output.

Usage:
    python clear_image.py <path_to_your_image>

Example:
    python clear_image.py my_blurry_photo.jpg
"""

import cv2
import sys
import os


def clear_image(image_path):
    """
    Takes a blurry/dark image and applies multiple enhancement techniques
    to make it readable and clear.

    Args:
        image_path (str): Path to the input image file.

    Returns:
        None — displays all processed images in separate windows.
    """

    # ──────────────────────────────────────────────
    #  Step 1: Read the image
    # ──────────────────────────────────────────────
    img = cv2.imread(image_path)

    if img is None:
        print(f"❌ Error: Could not read image at '{image_path}'")
        print("   Make sure the file exists and is a valid image format.")
        sys.exit(1)

    print(f"✅ Image loaded successfully: {image_path}")
    print(f"   Dimensions: {img.shape[1]}x{img.shape[0]} pixels")

    # ──────────────────────────────────────────────
    #  Step 2: Convert to Grayscale
    # ──────────────────────────────────────────────
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # ──────────────────────────────────────────────
    #  Step 3: Apply Gaussian Blur (noise reduction)
    # ──────────────────────────────────────────────
    # Kernel size (21, 21) — larger kernel = more blur/smoothing
    # This helps remove noise before thresholding
    gaus = cv2.GaussianBlur(gray, (21, 21), 0)

    # ──────────────────────────────────────────────
    #  Step 4: Apply Thresholding Techniques
    # ──────────────────────────────────────────────

    # 🎯 Threshold Method 1: Simple Binary Threshold
    # Pixels above 127 → white (255), below → black (0)
    _, threshold = cv2.threshold(gaus, 127, 255, cv2.THRESH_BINARY)

    # 🎯 Threshold Method 2: Otsu's Binarization
    # Automatically finds the optimal threshold value
    _, threshold2 = cv2.threshold(gaus, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 🎯 Threshold Method 3: Adaptive Threshold
    # Uses local pixel neighborhood to determine threshold
    # Great for images with varying lighting conditions
    threshold3 = cv2.adaptiveThreshold(
        gaus, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11, 2
    )

    # ──────────────────────────────────────────────
    #  Step 5: Display all results
    # ──────────────────────────────────────────────
    print("\n🖼️  Showing results... Press any key to close all windows.\n")

    cv2.imshow("Original", img)
    cv2.imshow("Gaussian Blur", gaus)
    cv2.imshow("Threshold - Binary", threshold)
    cv2.imshow("Threshold - Otsu", threshold2)
    cv2.imshow("Threshold - Adaptive", threshold3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # ──────────────────────────────────────────────
    #  Step 6 (Optional): Save results
    # ──────────────────────────────────────────────
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    cv2.imwrite(f"{output_dir}/{base_name}_gaussian.jpg", gaus)
    cv2.imwrite(f"{output_dir}/{base_name}_threshold_binary.jpg", threshold)
    cv2.imwrite(f"{output_dir}/{base_name}_threshold_otsu.jpg", threshold2)
    cv2.imwrite(f"{output_dir}/{base_name}_threshold_adaptive.jpg", threshold3)

    print(f"💾 All processed images saved to '{output_dir}/' folder!")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("=" * 55)
        print("  🔍 Clear Your Image — Usage")
        print("=" * 55)
        print()
        print("  python clear_image.py <path_to_image>")
        print()
        print("  Example:")
        print("  python clear_image.py my_blurry_photo.jpg")
        print()
        print("=" * 55)
        sys.exit(1)

    clear_image(sys.argv[1])
