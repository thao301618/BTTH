import cv2
import numpy as np
from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk

class ImageSmoothingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Smoothing Application")
        self.root.geometry("800x600")
        
        self.image_label = Label(self.root)
        self.image_label.pack()

        self.open_button = Button(self.root, text="Open Image", command=self.open_image)
        self.open_button.pack(pady=10)

        self.average_button = Button(self.root, text="Average Blur", command=self.apply_average_blur)
        self.average_button.pack(pady=5)

        self.gaussian_button = Button(self.root, text="Gaussian Blur", command=self.apply_gaussian_blur)
        self.gaussian_button.pack(pady=5)

        self.median_button = Button(self.root, text="Median Blur", command=self.apply_median_blur)
        self.median_button.pack(pady=5)

        self.bilateral_button = Button(self.root, text="Bilateral Filter", command=self.apply_bilateral_filter)
        self.bilateral_button.pack(pady=5)

        self.save_button = Button(self.root, text="Save Image", command=self.save_image)
        self.save_button.pack(pady=10)

        self.original_image = None
        self.processed_image = None

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
        if file_path:
            self.original_image = cv2.imread(file_path)
            self.display_image(self.original_image)

    def display_image(self, image):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_pil = Image.fromarray(image_rgb)
        image_tk = ImageTk.PhotoImage(image_pil)
        self.image_label.configure(image=image_tk)
        self.image_label.image = image_tk

    def apply_average_blur(self):
        if self.original_image is not None:
            self.processed_image = cv2.blur(self.original_image, (5, 5))
            self.display_image(self.processed_image)

    def apply_gaussian_blur(self):
        if self.original_image is not None:
            self.processed_image = cv2.GaussianBlur(self.original_image, (5, 5), 0)
            self.display_image(self.processed_image)

    def apply_median_blur(self):
        if self.original_image is not None:
            self.processed_image = cv2.medianBlur(self.original_image, 5)
            self.display_image(self.processed_image)

    def apply_bilateral_filter(self):
        if self.original_image is not None:
            self.processed_image = cv2.bilateralFilter(self.original_image, 9, 75, 75)
            self.display_image(self.processed_image)

    def save_image(self):
        if self.processed_image is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")])
            if file_path:
                cv2.imwrite(file_path, self.processed_image)

if __name__ == "__main__":
    root = Tk()
    app = ImageSmoothingApp(root)
    root.mainloop()
