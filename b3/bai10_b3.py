import cv2
import numpy as np
from tkinter import Tk, filedialog
from matplotlib import pyplot as plt

# Hàm để chọn ảnh từ máy tính
def choose_image():
    Tk().withdraw()  # Tắt giao diện chính của tkinter
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    return file_path

# Hàm tăng cường ảnh bằng CLAHE
def enhance_image(image):
    # Chuyển đổi ảnh sang không gian màu YUV
    yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    
    # Tăng cường kênh độ sáng Y bằng CLAHE
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    yuv[:, :, 0] = clahe.apply(yuv[:, :, 0])
    
    # Chuyển ảnh về không gian màu BGR
    enhanced_image = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
    return enhanced_image

# Hiển thị ảnh gốc và ảnh đã tăng cường
def display_images(original, enhanced):
    # Chuyển đổi ảnh từ BGR sang RGB để hiển thị với matplotlib
    original_rgb = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
    enhanced_rgb = cv2.cvtColor(enhanced, cv2.COLOR_BGR2RGB)
    
    # Hiển thị ảnh
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Ảnh gốc")
    plt.imshow(original_rgb)
    plt.axis("off")
    
    plt.subplot(1, 2, 2)
    plt.title("Ảnh tăng cường")
    plt.imshow(enhanced_rgb)
    plt.axis("off")
    
    plt.tight_layout()
    plt.show()

# Chương trình chính
if __name__ == "__main__":
    file_path = choose_image()
    if file_path:
        # Đọc ảnh
        original_image = cv2.imread(file_path)
        
        # Tăng cường chất lượng ảnh
        enhanced_image = enhance_image(original_image)
        
        # Hiển thị ảnh
        display_images(original_image, enhanced_image)
    else:
        print("Bạn chưa chọn ảnh!")
