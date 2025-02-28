import tkinter as tk

# Hàm xử lý khi nhấn nút

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Ứng dụng quản lý danh bạ")
root.geometry("800x420")
root.configure(background="#242424")

# Tạo các widget
# label tiêu đề chính
label_main_content = tk.Label(root, bg="#242424", font=("Arial", 14, "bold"), text= "Quản lý danh bạ", fg="white")
label_main_content.pack(fill="x")

# Bố trí widget trên giao diện

# Chạy ứng dụng
root.mainloop()
