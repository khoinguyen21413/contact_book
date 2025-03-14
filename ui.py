import tkinter as tk
from tkinter import ttk, messagebox
from contact_form import ContactForm
from data import sample_contacts
from contact import Contact

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng dụng quản lý danh bạ")
        self.root.geometry("800x420")
        self.root.configure(background="#242424")

        # Frame tiêu đề
        frame_title = tk.Frame(root, bg="#242424")
        frame_title.pack(fill="x", pady=5)
        tk.Label(frame_title, bg="#242424", font=("Arial", 14, "bold"), text="Quản lý danh bạ", fg="white").pack(pady=5)

        # Frame bảng danh bạ
        frame_table = tk.Frame(root)
        frame_table.pack(side="left", fill="both", expand=True, padx=5)
        self.columns = ("Họ", "Tên", "Giới tính", "Số điện thoại", "Email", "Địa chỉ")
        self.tree = ttk.Treeview(frame_table, columns=self.columns, show="headings", height=8)

        for col in self.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100 if col == "Email" else 60)

        self.tree.pack(pady=5, fill="both", expand=True)

        # Thêm dữ liệu mẫu
        for contact in sample_contacts:
            self.tree.insert("", "end", values=contact.to_tuple())

        # Frame chứa các nút
        frame_button = tk.Frame(root, bg="#242424")
        frame_button.pack(side="right", fill='y', padx=5, pady=5)

        buttons = [("Tạo mới", self.create_contact), ("Sửa", self.edit_contact), ("Tìm kiếm", self.search_contact), ("Xóa", self.delete_contact)]
        for text, cmd in buttons:
            tk.Button(frame_button, text=text, width=15, command=cmd).pack(pady=15)

    def create_contact(self):
        ContactForm(self.root, self.tree)

    def edit_contact(self):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected, "values")
            ContactForm(self.root, self.tree, Contact(*values))
        else:
            messagebox.showwarning("Chú ý", "Vui lòng chọn một liên hệ để sửa")

    def search_contact(self):
        for item in self.tree.get_children():
            values = self.tree.item(item, "values")
            if "Nguyên" in values:
                self.tree.selection_set(item)
                self.tree.focus(item)
                return
        messagebox.showinfo("Thông báo","Không tìm thấy liên hệ")

    def delete_contact(self):
        selected = self.tree.selection()
        if selected:
            self.tree.delete(selected)
        else:
            messagebox.showwarning("Chú ý", "Vui lòng chọn một liên hệ để xóa!")

