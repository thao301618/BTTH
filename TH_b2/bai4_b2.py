import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

import sympy

class DiemPythonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Báo cáo thống kê điểm")
        self.df = None

        # Tải dữ liệu mặc định
        self.load_file()

        # Các nút thống kê
        buttons = [
            ("Thống kê điểm", self.thong_ke_diem),
            ("Thống kê L1, L2", self.thong_ke_l1_l2),
            ("Thống kê các bài kiểm tra", self.thong_ke_kiem_tra),
            ("Thống kê theo lớp", self.thong_ke_theo_lop)
        ]
        for text, command in buttons:
            tk.Button(self.root, text=text, command=command).pack(pady=5)

        # Bảng hiển thị kết quả
        self.tree = ttk.Treeview(self.root, columns=("Tiêu đề", "Giá trị"), show='headings', height=10)
        self.tree.column("Tiêu đề", anchor=tk.W, width=200)
        self.tree.column("Giá trị", anchor=tk.W, width=150)
        self.tree.heading("Tiêu đề", text="Tiêu đề")
        self.tree.heading("Giá trị", text="Giá trị")
        self.tree.pack(pady=10)

    def load_file(self):

        try:
            self.df = pd.read_csv(r"D:\MNM\TH\b2\diemPython.csv", index_col=0, header=0)
            messagebox.showinfo("Thành công", "Dữ liệu đã được tải thành công từ tệp diemPython.csv.")
        except FileNotFoundError:
            messagebox.showerror("Lỗi", "Không tìm thấy tệp diemPython.csv.")

    def thong_ke_diem(self):
        """Thống kê số lượng sinh viên đạt các loại điểm."""
        if self.df is not None:
            # Các loại điểm
            categories = ['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
            values = [np.sum(self.df[f'Loại {category}'].values) for category in categories]

            # Hiển thị trong bảng
            self.tree.delete(*self.tree.get_children())
            for category, value in zip(categories, values):
                self.tree.insert("", "end", values=(f"Tổng sinh viên đạt điểm {category}", value))

            # Vẽ đồ thị
            self.plot_bar_chart(categories, values, "Thống kê số lượng sinh viên đạt các mức điểm", "Loại điểm", "Số sinh viên")

    def thong_ke_l1_l2(self):
        """Thống kê chuẩn đầu ra L1, L2."""
        if self.df is not None:
            categories = ['L1', 'L2']
            values = [np.sum(self.df[category].values) for category in categories]

            # Hiển thị trong bảng
            self.tree.delete(*self.tree.get_children())
            for category, value in zip(categories, values):
                self.tree.insert("", "end", values=(f"Tổng điểm {category}", value))

            # Vẽ đồ thị
            self.plot_bar_chart(categories, values, "Thống kê chuẩn đầu ra L1, L2", "Chuẩn đầu ra", "Tổng điểm")

    def thong_ke_kiem_tra(self):
        """Thống kê các bài kiểm tra."""
        if self.df is not None:
            categories = ['TX1', 'TX2', 'Cuối kỳ']
            values = [np.mean(self.df[category].values) for category in categories]

            # Hiển thị trong bảng
            self.tree.delete(*self.tree.get_children())
            for category, value in zip(categories, values):
                self.tree.insert("", "end", values=(f"Điểm trung bình {category}", value))

            # Vẽ đồ thị
            self.plot_bar_chart(categories, values, "Thống kê điểm trung bình các bài kiểm tra", "Bài kiểm tra", "Điểm trung bình")

    def thong_ke_theo_lop(self):
        """Thống kê theo lớp cho tất cả các loại điểm."""
        if self.df is not None:
            # Lấy dữ liệu các loại điểm
            categories = ['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
            diem_data = {category: self.df[f'Loại {category}'].values for category in categories}

            # Tìm lớp có số sinh viên đạt điểm A nhiều nhất
            maxA = diem_data['A'].max()
            index_maxA = np.where(diem_data['A'] == maxA)[0][0]
            lop_maxA = self.df.iloc[index_maxA, 0]  # Mã lớp có nhiều sinh viên đạt điểm A

            # Hiển thị trong bảng
            self.tree.delete(*self.tree.get_children())
            self.tree.insert("", "end", values=("Lớp có nhiều sinh viên đạt điểm A", lop_maxA, maxA))

            # Tìm lớp có số sinh viên đạt điểm B+ nhiều nhất
            maxB_plus = diem_data['B+'].max()
            index_maxB_plus = np.where(diem_data['B+'] == maxB_plus)[0][0]
            lop_maxB_plus = self.df.iloc[index_maxB_plus, 0]  # Mã lớp có nhiều sinh viên đạt điểm B+

            # Hiển thị trong bảng
            self.tree.insert("", "end", values=("Lớp có nhiều sinh viên đạt điểm B+", lop_maxB_plus, maxB_plus))

            # Tìm lớp có số sinh viên đạt điểm B nhiều nhất
            maxB = diem_data['B'].max()
            index_maxB = np.where(diem_data['B'] == maxB)[0][0]
            lop_maxB = self.df.iloc[index_maxB, 0]  # Mã lớp có nhiều sinh viên đạt điểm B

            # Hiển thị trong bảng
            self.tree.insert("", "end", values=("Lớp có nhiều sinh viên đạt điểm B", lop_maxB, maxB))

            # Tìm lớp có số sinh viên đạt điểm C+ nhiều nhất
            maxC_plus = diem_data['C+'].max()
            index_maxC_plus = np.where(diem_data['C+'] == maxC_plus)[0][0]
            lop_maxC_plus = self.df.iloc[index_maxC_plus, 0]  # Mã lớp có nhiều sinh viên đạt điểm C+

            # Hiển thị trong bảng
            self.tree.insert("", "end", values=("Lớp có nhiều sinh viên đạt điểm C+", lop_maxC_plus, maxC_plus))

            # Tìm lớp có số sinh viên đạt điểm C nhiều nhất
            maxC = diem_data['C'].max()
            index_maxC = np.where(diem_data['C'] == maxC)[0][0]
            lop_maxC = self.df.iloc[index_maxC, 0]  # Mã lớp có nhiều sinh viên đạt điểm C

            # Hiển thị trong bảng
            self.tree.insert("", "end", values=("Lớp có nhiều sinh viên đạt điểm C", lop_maxC, maxC))

            # Tìm lớp có số sinh viên đạt điểm D+ nhiều nhất
            maxD_plus = diem_data['D+'].max()
            index_maxD_plus = np.where(diem_data['D+'] == maxD_plus)[0][0]
            lop_maxD_plus = self.df.iloc[index_maxD_plus, 0]  # Mã lớp có nhiều sinh viên đạt điểm D+

            # Hiển thị trong bảng
            self.tree.insert("", "end", values=("Lớp có nhiều sinh viên đạt điểm D+", lop_maxD_plus, maxD_plus))

            # Tìm lớp có số sinh viên đạt điểm D nhiều nhất
            maxD = diem_data['D'].max()
            index_maxD = np.where(diem_data['D'] == maxD)[0][0]
            lop_maxD = self.df.iloc[index_maxD, 0]  # Mã lớp có nhiều sinh viên đạt điểm D

            # Hiển thị trong bảng
            self.tree.insert("", "end", values=("Lớp có nhiều sinh viên đạt điểm D", lop_maxD, maxD))

            # Tìm lớp có số sinh viên đạt điểm F nhiều nhất
            maxF = diem_data['F'].max()
            index_maxF = np.where(diem_data['F'] == maxF)[0][0]
            lop_maxF = self.df.iloc[index_maxF, 0]  # Mã lớp có nhiều sinh viên đạt điểm F

            # Hiển thị trong bảng
            self.tree.insert("", "end", values=("Lớp có nhiều sinh viên đạt điểm F", lop_maxF, maxF))


            # Vẽ biểu đồ đường cho các loại điểm
            self.plot_line_chart(diem_data, "Thống kê theo lớp", "Lớp", "Số sinh viên đạt điểm")

    def plot_bar_chart(self, categories, values, title, xlabel, ylabel):
        """Vẽ biểu đồ cột."""
        plt.figure(figsize=(10, 6))
        plt.bar(categories, values, color='skyblue')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_line_chart(self, diem_data, title, xlabel, ylabel):
        """Vẽ biểu đồ đường cho các loại điểm."""
        plt.figure(figsize=(10, 6))
        for category, values in diem_data.items():
            plt.plot(range(len(values)), values, label=f"Điểm {category}")

        # Đặt nhãn và tiêu đề
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend(loc='upper right')
        plt.title(title)
        plt.tight_layout()
        plt.show()

# Khởi chạy ứng dụng
if __name__ == "__main__":
    root = tk.Tk()
    app = DiemPythonApp(root)
    root.mainloop()
