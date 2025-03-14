import tkinter as tk
from tkinter import ttk, messagebox
from contact import Contact

class ContactForm(tk.Toplevel):
    def __init__(self, root, tree, contact=None):
        super().__init__(root)
        self.title("Tạo mới" if contact is None else "Chỉnh sửa")
        self.geometry("300x400")
        self.tree = tree
        self.contact = contact

        # Tiêu đề
        tk.Label(self, text="Tạo mới" if contact is None else "Chỉnh sửa", 
                 bg="lightgreen", font=("Arial", 14, "bold")).pack(fill="x", pady=5)

        # Các trường nhập liệu
        self.entries = {}
        fields = ["Họ", "Tên", "Số điện thoại", "Email", "Địa chỉ"]
        for field in fields:
            frame = tk.Frame(self)
            frame.pack(fill="x", padx=15, pady=2)
            tk.Label(frame, text=field).pack(side="left")
            entry = tk.Entry(frame)
            entry.pack(side="right", fill="x", expand=True)
            self.entries[field] = entry
        
        # Giới tính
        self.gender_var = tk.StringVar(value="Nam")
        tk.Label(self, text="Giới tính:").pack(anchor="w", padx=15, pady=2)
        frame_gender = tk.Frame(self)
        frame_gender.pack(fill="x", padx=15, pady=5)
        tk.Radiobutton(frame_gender, text="Nam", variable=self.gender_var, value="Nam").pack(side="left", padx=5)
        tk.Radiobutton(frame_gender, text="Nữ", variable=self.gender_var, value="Nữ").pack(side="left", padx=5)

        # Nếu chỉnh sửa, điền sẵn dữ liệu
        if contact:
            self.entries["Họ"].insert(0, contact.last_name)
            self.entries["Tên"].insert(0, contact.first_name)
            self.entries["Số điện thoại"].insert(0, contact.phone)
            self.entries["Email"].insert(0, contact.email)
            self.entries["Địa chỉ"].insert(0, contact.address)
            self.gender_var.set(contact.gender)

        # Nút Thêm hoặc Cập nhật
        btn_text = "Thêm" if contact is None else "Cập nhật"
        tk.Button(self, text=btn_text, width=15, command=self.save_contact).pack(pady=10)

    def save_contact(self):
        values = (
            self.entries["Họ"].get(),
            self.entries["Tên"].get(),
            self.gender_var.get(),
            self.entries["Số điện thoại"].get(),
            self.entries["Email"].get(),
            self.entries["Địa chỉ"].get(),
        )

        if all(values):
            contact = Contact(*values)
            if self.contact:  # Chỉnh sửa
                selected = self.tree.selection()
                self.tree.item(selected, values=contact.to_tuple())
            else:  # Thêm mới
                self.tree.insert("", "end", values=contact.to_tuple())
            self.destroy()
        else:
            messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            self.lift()
            self.focus_force()
