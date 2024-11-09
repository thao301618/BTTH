import tkinter as tk
from tkinter import messagebox
import numpy as np

class EquationSolverApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Giải hệ phương trình")
        self.coefficients = []  # Lưu các ô nhập hệ số
        self.results = []  # Lưu các ô nhập kết quả

        self.create_widgets()

    def create_widgets(self):
        self.equation_frame = tk.Frame(self.master)
        self.equation_frame.pack()

        tk.Label(self.master, text="Nhập số lượng phương trình:").pack()
        self.num_eq_entry = tk.Entry(self.master)
        self.num_eq_entry.pack()

        self.create_matrix_button = tk.Button(self.master, text="Tạo phương trình",
                                              command=self.create_equation_entries)
        self.create_matrix_button.pack()

        self.solve_button = tk.Button(self.master, text="Giải hệ phương trình", command=self.solve_equations)
        self.solve_button.pack()

        self.clear_entries_button = tk.Button(self.master, text="Xóa Dữ Liệu", command=self.clear_all_entries)
        self.clear_entries_button.pack()

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

    def create_equation_entries(self):
        try:
            num_eq = int(self.num_eq_entry.get())
            self.clear_entries()

            for i in range(num_eq):
                row_frame = tk.Frame(self.equation_frame)
                row_frame.pack()

                row = []
                for j in range(num_eq):
                    coef_entry = tk.Entry(row_frame, width=5)
                    coef_entry.pack(side=tk.LEFT)

                    # Thêm nhãn cho ẩn của phương trình (x1, x2, ...)
                    if j < num_eq - 1:
                        var_label = tk.Label(row_frame, text=f"x{j + 1} +")
                    else:
                        var_label = tk.Label(row_frame, text=f"x{j + 1}")  # Không thêm dấu "+" ở hệ số cuối
                    var_label.pack(side=tk.LEFT)

                    row.append(coef_entry)

                # Thêm dấu "=" và ô nhập kết quả
                equal_label = tk.Label(row_frame, text=" = ")
                equal_label.pack(side=tk.LEFT)

                result_entry = tk.Entry(row_frame, width=5)  # Ô nhập kết quả
                result_entry.pack(side=tk.LEFT)

                self.coefficients.append(row)
                self.results.append(result_entry)
        except ValueError:
            messagebox.showerror("Error", "Vui lòng nhập số hợp lệ.")

    def clear_entries(self):
        for widget in self.equation_frame.winfo_children():
            widget.destroy()
        self.coefficients.clear()
        self.results.clear()

    def clear_all_entries(self):
        for row_entries in self.coefficients:
            for coef_entry in row_entries:
                coef_entry.delete(0, tk.END)  # Xóa dữ liệu trong ô nhập hệ số

        for result_entry in self.results:
            result_entry.delete(0, tk.END)  # Xóa dữ liệu trong ô nhập kết quả

    def solve_equations(self):
        try:
            A = []
            B = []

            # Lấy hệ số và kết quả từ các ô nhập và đánh giá biểu thức toán học
            for row_entries, result_entry in zip(self.coefficients, self.results):
                row = [float(eval(coef.get())) for coef in row_entries]  # Sử dụng eval() để đánh giá biểu thức
                c = float(eval(result_entry.get()))  # Sử dụng eval() cho kết quả
                A.append(row)
                B.append(c)

            A = np.array(A)
            B = np.array(B)

            rank_A = np.linalg.matrix_rank(A)
            if rank_A < A.shape[1]:  # Nếu rank < số cột, hệ phương trình có vô số nghiệm
                self.result_label.config(text="Hệ phương trình có vô số nghiệm.")
            else:
                det = np.linalg.det(A)
                if det == 0:
                    self.result_label.config(text="Hệ phương trình vô nghiệm.")
                else:
                    solution = np.linalg.solve(A, B)
                    result_text = ', '.join([f"x{i + 1} = {solution[i]:.2f}" for i in range(len(solution))])
                    self.result_label.config(text=result_text)

        except Exception as e:
            messagebox.showerror("Error", f"Không thể giải được hệ phương trình: {e}")

# Tạo cửa sổ ứng dụng
root = tk.Tk()
app = EquationSolverApp(root)
root.mainloop()