import tkinter as tk
from tkinter import ttk, messagebox

def open_create_window():
    """Mở cửa sổ nhập thông tin khi nhấn 'Tạo mới'."""
    create_window = tk.Toplevel(root)
    create_window.title("Tạo mới")
    create_window.geometry("300x400")

    # Tiêu đề
    tk.Label(create_window, text="Tạo mới", bg="lightgreen", font=("Arial", 14, "bold")).pack(fill="x", pady=5)

    # Nhãn và ô nhập dữ liệu
    labels = ["Họ", "Tên", "Số điện thoại", "Email", "Địa chỉ"]
    entries = {}

    for i, label in enumerate(labels):
        tk.Label(create_window, text=label, font=("Arial", 10)).pack(anchor="w", padx=10, pady=2)
        entry = tk.Entry(create_window, width=30)
        entry.pack(padx=10, pady=2)
        entries[label] = entry

    # Giới tính
    gender_var = tk.StringVar()
    tk.Label(create_window, text="Giới tính", font=("Arial", 10)).pack(anchor="w", padx=10, pady=2)

    frame_gender = tk.Frame(create_window)
    frame_gender.pack(pady=5)
    tk.Radiobutton(frame_gender, text="Nam", variable=gender_var, value="Nam").pack(side="left", padx=5)
    tk.Radiobutton(frame_gender, text="Nữ", variable=gender_var, value="Nữ").pack(side="left", padx=5)

    def add_contact():
        """Thêm dữ liệu vào bảng danh bạ"""
        values = (
            entries["Họ"].get(),
            entries["Tên"].get(),
            gender_var.get(),
            entries["Số điện thoại"].get(),
            entries["Email"].get(),
            entries["Địa chỉ"].get()
        )
        if all(values):
            tree.insert("", "end", values=values)
            create_window.destroy()
        else:
            messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ thông tin!")

    # Nút "Thêm"
    btn_add = tk.Button(create_window, text="Thêm", command=add_contact, width=15)
    btn_add.pack(pady=10)

# ===== Cửa sổ chính =====
root = tk.Tk()
root.title("Quản lý danh bạ")
root.geometry("700x450")

# ===== FRAME 1: Chứa tiêu đề =====
frame_title = tk.Frame(root, bg="white")
frame_title.pack(fill="x", pady=5)

title_label = tk.Label(frame_title, text="Quản lý danh bạ", font=("Arial", 14, "bold"), bg="white")
title_label.pack(pady=5)

# ===== FRAME 2: Chứa bảng danh bạ =====
frame_table = tk.Frame(root, bg="white")
frame_table.pack(side="left", fill="both", expand=True, padx=10, pady=5)

columns = ("Họ", "Tên", "Giới tính", "Số điện thoại", "Email", "Địa chỉ")
tree = ttk.Treeview(frame_table, columns=columns, show="headings", height=8)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack(padx=5, pady=5, fill="both", expand=True)

# ===== FRAME 3: Chứa các nút chức năng =====
frame_buttons = tk.Frame(root, bg="black")
frame_buttons.pack(side="right", fill="y", padx=10, pady=10)

btn_them = tk.Button(frame_buttons, text="Tạo mới", command=open_create_window, width=15)
btn_them.pack(pady=10)

# Chạy chương trình
root.mainloop()
