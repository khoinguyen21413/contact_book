import tkinter as tk
from tkinter import ttk,messagebox
import random

# code event cho 4 nút
def create_contact():
    
    # tree.insert("", "end", values=random.choice(data_samples))

    # Khi insert, hiển thị cửa sổ khác (cửa sổ add) nhập các giá trị vào ô input.
    # Nhan vao o Them de them du lieu vao bang


    # """Mở cửa sổ nhập thông tin khi nhấn 'Tạo mới'."""
    create_window = tk.Toplevel(root)
    create_window.title("Tạo mới")
    create_window.geometry("300x400")

    # Tiêu đề
    tk.Label(create_window, text="Tạo mới", bg="lightgreen", font=("Arial", 14, "bold")).pack(fill="x", pady=5)

    # Họ
    frame_lastname = tk.Frame(create_window)
    frame_lastname.pack(fill="x", padx=15, pady=2)
    tk.Label(frame_lastname, text="Họ").pack(side="left")
    entry_lastname = tk.Entry(frame_lastname)
    entry_lastname.pack(side="right", fill="x", expand=True)

    # Tên
    frame_firstname = tk.Frame(create_window)
    frame_firstname.pack(fill="x", padx=15, pady=2)
    tk.Label(frame_firstname, text="Tên").pack(side="left")
    entry_firstname = tk.Entry(frame_firstname)
    entry_firstname.pack(side="right", fill="x", expand=True)

    # Giới tính
    gender_var = tk.StringVar(value="Nam")  # Đặt giá trị mặc định là "Nam"
    tk.Label(create_window, text="Giới tính:", font=("Arial", 10)).pack(anchor="w", padx=15, pady=2)

    frame_gender = tk.Frame(create_window)
    frame_gender.pack(fill="x", padx=15, pady=5)
    tk.Radiobutton(frame_gender, text="Nam", variable=gender_var, value="Nam").pack(side="left", padx=5)
    tk.Radiobutton(frame_gender, text="Nữ", variable=gender_var, value="Nữ").pack(side="left", padx=5)

    # Số điện thoại
    frame_phone = tk.Frame(create_window)
    frame_phone.pack(fill="x", padx=15, pady=2)
    tk.Label(frame_phone, text="Số điện thoại").pack(side="left")
    entry_phone = tk.Entry(frame_phone)
    entry_phone.pack(side="right", fill="x", expand=True)

    # Email
    frame_email = tk.Frame(create_window)
    frame_email.pack(fill="x", padx=15, pady=2)
    tk.Label(frame_email, text="Email").pack(side="left")
    entry_email = tk.Entry(frame_email)
    entry_email.pack(side="right", fill="x", expand=True)

    # Địa chỉ
    frame_address = tk.Frame(create_window)
    frame_address.pack(fill="x", padx=15, pady=2)
    tk.Label(frame_address, text="Địa chỉ").pack(side="left")
    entry_address = tk.Entry(frame_address)
    entry_address.pack(side="right", fill="x", expand=True)

    # Function to add new contact
    def add_contact():
        values = (
            entry_lastname.get(),
            entry_firstname.get(),
            gender_var.get(),
            entry_phone.get(),
            entry_email.get(),
            entry_address.get()
        )

        if all(values):
            tree.insert("", "end", values=values)
            # Hủy cửa sổ khi nhập đầy đủ dữ liệu
            create_window.destroy()
        else:
            messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            create_window.lift()  # Đưa cửa sổ lên trên cùng
            create_window.focus_force()  # Đặt focus vào cửa sổ

    btn_add = tk.Button(create_window, text= "Thêm", width= 15, command= add_contact)
    btn_add.pack(pady=10)

def edit_contact():
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

# Danh sách dữ liệu mẫu
data_samples = [
    ("Nguyễn", "Nguyên", "Nam", "0903 612 345", "khoinguyen.21413@gmail.com", "Đà Nẵng"),
    ("Lê", "An", "Nữ", "0912 345 678", "lean@gmail.com", "Hà Nội"),
    ("Trần", "Bình", "Nam", "0987 654 321", "tranbinh@gmail.com", "TP Hồ Chí Minh"),
    ("Phạm", "Thảo", "Nữ", "0971 223 456", "phamthao99@gmail.com", "Đà Nẵng"),
    ("Hoàng", "Dũng", "Nam", "0904 778 899", "hoangdung@gmail.com", "Hải Phòng"),
    ("Vũ", "Linh", "Nữ", "0965 112 223", "vulinh@gmail.com", "Cần Thơ"),
]

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
tk.Label(frame_title, bg=colour_black, font=("Arial", 14, "bold"), text= "Quản lý danh bạ", fg="white").pack(pady=5)

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
for value in data_samples:
    tree.insert("", "end", values=value)

# frame chứa 4 nút theo hàng dọc
frame_button = tk.Frame(root, bg= colour_black)
frame_button.pack(side= "right", fill='y',padx= 5,pady=5)

# code giao diện cho 4 nút
btn_them = tk.Button(master= frame_button, bg= colour_white,
                    text= "Tạo mới",width= 15, command= create_contact)
btn_them.pack(pady= 30)

btn_edit_contact = tk.Button(master= frame_button, bg= colour_white,
                    text= "Sửa", width= 15, command= edit_contact)
btn_edit_contact.pack(pady= 30)

btn_tim_kiem = tk.Button(master= frame_button, bg= colour_white,
                    text= "Tìm kiếm", width= 15, command= tim_kiem)
btn_tim_kiem.pack(pady= 30)

btn_xoa = tk.Button(master= frame_button,bg= colour_white,
                    text= "Xóa", width= 15, command= xoa)
btn_xoa.pack(pady= 30)

# Chạy ứng dụng
root.mainloop()
