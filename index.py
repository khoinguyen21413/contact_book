import tkinter as tk

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


# Bố trí widget trên giao diện

# Chạy ứng dụng
root.mainloop()
