import cv2
import numpy as np
from tkinter import Tk, filedialog
from matplotlib import pyplot as plt

def main():
    # Tạo cửa sổ chọn ảnh
    root = Tk()
    root.withdraw()  # Ẩn cửa sổ chính của Tkinter
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])

    if not file_path:
        print("Không có ảnh nào được chọn.")
        return

    # Đọc ảnh từ file
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print("Không thể đọc ảnh. Vui lòng kiểm tra lại.")
        return

    # 1. Phương pháp Canny Edge Detection
    edges_canny = cv2.Canny(img, 100, 200)

    # 2. Phương pháp Sobel Operator
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  # Biên theo trục X
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)  # Biên theo trục Y
    sobel = cv2.magnitude(sobel_x, sobel_y)  # Tổng hợp biên từ X và Y

    # 3. Phương pháp Laplacian Operator
    laplacian = cv2.Laplacian(img, cv2.CV_64F, ksize=3)

    # Hiển thị kết quả
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(img, cmap="gray")
    plt.title("Ảnh gốc")
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.imshow(edges_canny, cmap="gray")
    plt.title("Canny Edge Detection")
    plt.axis("off")

    plt.subplot(2, 2, 3)
    plt.imshow(sobel, cmap="gray")
    plt.title("Sobel Operator")
    plt.axis("off")

    plt.subplot(2, 2, 4)
    plt.imshow(laplacian, cmap="gray")
    plt.title("Laplacian Operator")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
