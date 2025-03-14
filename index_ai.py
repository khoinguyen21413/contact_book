import tkinter as tk
from tkinter import ttk, messagebox

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Quản lý danh bạ")
root.geometry("700x450")
root.configure(bg="black")

# ===== FRAME 1: Chứa tiêu đề =====
frame_title = tk.Frame(root, bg="white")
frame_title.pack(fill="x", pady=5)

title_label = tk.Label(frame_title, text="Quản lý danh bạ", font=("Arial", 14, "bold"), bg="white")
title_label.pack(pady=5)

# ===== FRAME 2: Chứa bảng danh bạ =====
frame_table = tk.Frame(root, bg="white")
frame_table.pack(side="left", fill="both", expand=True, padx=10, pady=5)

# Tạo Treeview để hiển thị danh bạ
columns = ("Họ", "Tên", "Giới tính", "Số điện thoại", "Email", "Địa chỉ")
tree = ttk.Treeview(frame_table, columns=columns, show="headings", height=8)

# Định dạng cột
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack(padx=5, pady=5, fill="both", expand=True)

# Thêm dữ liệu mẫu
tree.insert("", "end", values=("Nguyễn", "Nguyên", "Nam", "0903 612 345", "khoinguyen.21413@gmail.com", "Hòa Khương, Hòa Vang"))

# ===== FRAME 3: Chứa các nút chức năng theo hàng dọc =====
frame_buttons = tk.Frame(root, bg="black")
frame_buttons.pack(side="right", fill="y", padx=10, pady=10)

# Các hàm chức năng
def them_moi():
    tree.insert("", "end", values=("Lê", "An", "Nữ", "0912 345 678", "lean@gmail.com", "Hà Nội"))
    
def sua():
    selected_item = tree.selection()
    if selected_item:
        tree.item(selected_item, values=("Trần", "Bình", "Nam", "0987 654 321", "tranbinh@gmail.com", "TPHCM"))
    else:
        messagebox.showwarning("Chú ý", "Vui lòng chọn một liên hệ để sửa!")

def tim_kiem():
    for item in tree.get_children():
        values = tree.item(item, "values")
        if "Nguyên" in values:  # Giả sử tìm kiếm theo tên
            tree.selection_set(item)
            tree.focus(item)
            return
    messagebox.showinfo("Thông báo", "Không tìm thấy liên hệ!")

def xoa():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)
    else:
        messagebox.showwarning("Chú ý", "Vui lòng chọn một liên hệ để xóa!")

# Tạo các nút chức năng theo hàng dọc
btn_them = tk.Button(frame_buttons, text="Tạo mới", command=them_moi, width=15)
btn_them.pack(pady=10)

btn_sua = tk.Button(frame_buttons, text="Sửa", command=sua, width=15)
btn_sua.pack(pady=10)

btn_tim = tk.Button(frame_buttons, text="Tìm kiếm", command=tim_kiem, width=15)
btn_tim.pack(pady=10)

btn_xoa = tk.Button(frame_buttons, text="Xóa", command=xoa, width=15)
btn_xoa.pack(pady=10)

# Chạy chương trình
root.mainloop()
