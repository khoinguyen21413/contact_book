import tkinter as tk
from tkinter import ttk,messagebox
import random

# Danh sách dữ liệu mẫu
data_samples = [
    ("Nguyễn", "Nguyên", "Nam", "0903 612 345", "khoinguyen.21413@gmail.com", "Đà Nẵng"),
    ("Lê", "An", "Nữ", "0912 345 678", "lean@gmail.com", "Hà Nội"),
    ("Trần", "Bình", "Nam", "0987 654 321", "tranbinh@gmail.com", "TP Hồ Chí Minh"),
    ("Phạm", "Thảo", "Nữ", "0971 223 456", "phamthao99@gmail.com", "Đà Nẵng"),
    ("Hoàng", "Dũng", "Nam", "0904 778 899", "hoangdung@gmail.com", "Hải Phòng"),
    ("Vũ", "Linh", "Nữ", "0965 112 223", "vulinh@gmail.com", "Cần Thơ"),
]

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
    if col == "Email":
        tree.column(col, width=150)
    elif col == "Địa chỉ":
        tree.column(col, width=200)
    else:
        tree.column(col, width=60)

tree.pack(pady= 5, fill="both",expand=True)

# Thêm 5 dữ liệu ngẫu nhiên vào danh bạ
for _ in range(5):
    tree.insert("", "end", values=random.choice(data_samples))

# frame chứa 4 nút theo hàng dọc
frame_button = tk.Frame(root, bg= colour_black)
frame_button.pack(side= "right", fill='y',padx= 5,pady=5)

# code event cho 4 nút
def them():
    tree.insert("", "end", values=random.choice(data_samples))

def sua():
    selected_item = tree.selection()
    if selected_item:
        tree.item(selected_item, values=random.choice(data_samples))
    else:
        messagebox.showwarning("Chú ý", "Vui lòng chọn một người để sửa")

def tim_kiem():
    for item in tree.get_children():
        values = tree.item(item, "values")
        if "Nguyên" in values:
            tree.selection_set(item)
            tree.focus(item)
            return
    messagebox.showinfo("Thông báo","Không tìm thấy liên hệ")

def xoa():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)
    else:
        messagebox.showwarning("Chú ý", "Vui lòng chọn một liên hệ để xóa!")

# Chạy ứng dụng
root.mainloop()
