import tkinter as tk
from tkinter import ttk

# Hàm xử lý khi nhấn nút

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Ứng dụng quản lý danh bạ-by khoinguyen-v1")
root.geometry("800x420")
root.configure(background="#242424")

# Tạo các biến
colour_white = "white"
colour_black = "#242424"

# Tạo các widget
# Tạo frame chứa tiêu đề
frame_title = tk.Frame(root, bg=colour_black)
frame_title.pack(fill="x", pady= 5)

# Label tiêu đề chính
title_label = tk.Label(frame_title, bg=colour_black, font=("Arial", 14, "bold"), text= "Quản lý danh bạ", fg="white")
title_label.pack(pady=5)

# Tạo frame chứa bảng danh bạ
frame_table = tk.Frame(root)
frame_table.pack(side="left", fill="both",expand=True, padx= 5)

# tạo bảng danh bạ
columns = ("Họ", "Tên", "Giới tính","Số điện thoại", "Email", "Địa chỉ")
tree = ttk.Treeview(frame_table, columns=columns, show="headings", height=8)

# tạo cột
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)

tree.pack(pady= 5, fill="both",expand=True)

# Bố trí widget trên giao diện

# Chạy ứng dụng
root.mainloop()
