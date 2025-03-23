import tkinter as tk
from tkinter import ttk, messagebox
from contact_form import ContactForm
import database as db
from contact import Contact
from search_contact_form import Search_contact

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng dụng quản lý danh bạ")
        self.root.geometry("800x420")
        self.root.configure(background="#242424")
        self.create_menu()

        # Frame tiêu đề
        frame_title = tk.Frame(root, bg="#242424")
        frame_title.pack(fill="x", pady=5)
        tk.Label(frame_title, bg="#242424", font=("Arial", 14, "bold"), text="Quản lý danh bạ", fg="white").pack(pady=5)

        # Frame bảng danh bạ
        frame_table = tk.Frame(root)
        frame_table.pack(side="left", fill="both", expand=True, padx=5)
        self.columns = ("Id","Họ", "Tên", "Giới tính", "Số điện thoại", "Email", "Địa chỉ")
        self.tree = ttk.Treeview(frame_table, columns=self.columns, show="headings", height=8)

        for col in self.columns:
            self.tree.heading(col, text=col)
            if col != "Id":
                self.tree.column(col, width=100 if col == "Email" else 50)
            else:
                self.tree.column(col, width=20)

        self.tree.pack(pady=5, fill="both", expand=True)

        # # Thêm dữ liệu mẫu
        # for contact in sample_contacts:
        #     self.tree.insert("", "end", values=contact.to_tuple())

        # thêm dữ liệu từ database contact
        self.display_contacts()

        # Frame chứa các nút
        frame_button = tk.Frame(root, bg="#242424")
        frame_button.pack(side="right", fill='y', padx=5, pady=5)

        buttons = [("Tạo mới", self.create_contact), ("Sửa", self.edit_contact), ("Tìm kiếm", self.search_contact), ("Xóa", self.delete_contact)]
        for text, cmd in buttons:
            tk.Button(frame_button, text=text, width=15, command=cmd).pack(pady=15)

    def create_menu(self):
        """Tạo thanh menu cho ứng dụng"""
        menu_bar = tk.Menu(self.root)

        # Menu File
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Tạo mới", command=self.create_contact)
        file_menu.add_command(label="Sửa", command=self.edit_contact)
        file_menu.add_command(label="Xóa", command=self.delete_contact)
        file_menu.add_separator()
        file_menu.add_command(label="Thoát", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Menu Tìm kiếm
        search_menu = tk.Menu(menu_bar, tearoff=0)
        search_menu.add_command(label="Tìm kiếm liên hệ", command=self.search_contact)
        menu_bar.add_cascade(label="Tìm kiếm", menu=search_menu)

        # Menu Trợ giúp
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Hướng dẫn", command=self.show_help)
        help_menu.add_command(label="Thông tin", command=self.show_about)
        menu_bar.add_cascade(label="Trợ giúp", menu=help_menu)

        # Gán menu vào ứng dụng
        self.root.config(menu=menu_bar)

    def show_help(self):
        """Hiển thị hộp thoại hướng dẫn sử dụng"""
        messagebox.showinfo("Hướng dẫn", "Ứng dụng giúp quản lý danh bạ. Bạn có thể thêm, sửa, xóa và tìm kiếm liên hệ.")

    def show_about(self):
        """Hiển thị thông tin ứng dụng"""
        messagebox.showinfo("Giới thiệu", "Ứng dụng Quản lý Danh bạ\nPhiên bản 1.1\nTác giả: Khoi Nguyen")

    
    def display_contacts(self):
        """Hiển thị dữ liệu từ database lên TreeView."""
        self.tree.delete(*self.tree.get_children())  # Xóa dữ liệu cũ
        for row in db.get_all_contacts():
            self.tree.insert("", "end", values=row)

    def create_contact(self):
        ContactForm(self.root, self.tree)
        self.display_contacts()

    def edit_contact(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Lỗi", "Vui lòng chọn một liên hệ để chỉnh sửa!")
            return
        values = self.tree.item(selected[0], "values")
        contact = Contact(*values)
        ContactForm(self.root, self.tree, contact)

    def search_contact(self):
        Search_contact(self.root, self.tree)

    def delete_contact(self):
        selected = self.tree.selection()
        values = self.tree.item(selected[0], "values")

        contact = Contact(*values)
        if selected:
            if not values:
                messagebox.showerror("Lỗi", "Không thể lấy thông tin liên hệ để xóa.")
                return     
            # Xác nhận xóa
            if messagebox.askyesno("Xác nhận", f"Bạn có chắc chắn muốn xóa ID {contact.id} không?"):
                db.delete_contact(contact.id)
                self.display_contacts()
            return
        else:
            messagebox.showwarning("Chú ý", "Vui lòng chọn một liên hệ để xóa!")

