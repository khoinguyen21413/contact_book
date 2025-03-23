import tkinter as tk
from ui import ContactManagerApp
from database import create_db

# Chạy ứng dụng
if __name__ == "__main__":
    create_db()  # Tạo database nếu chưa có
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()
