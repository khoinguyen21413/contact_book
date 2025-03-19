import tkinter as tk
from tkinter import ttk, messagebox

# Lớp tìm kiếm danh bạ
class Search_contact(tk.Toplevel):
    def __init__(self, root, tree):
        super().__init__(root)
        self.tree = tree
        self.title('Tìm kiếm')
        self.geometry("300x120")

        frame = tk.Frame(self)
        frame.pack(fill="x", padx=15, pady=5)

        tk.Label(frame, text="Từ cần tìm:").pack(side="left")
        self.entry_search = tk.Entry(frame)
        self.entry_search.pack(side="right", fill="x", expand=True)

        btn_search = tk.Button(self, text="Tìm kiếm", width=15, command=self.search)
        btn_search.pack(pady=10)

    def search(self):
        values = self.entry_search.get().strip()
        if values:
            for item in self.tree.get_children():
                row_values = self.tree.item(item, "values")  # Lấy dữ liệu của hàng
                if any(values.lower() in str(value).lower() for value in row_values):
                    self.tree.selection_set(item)
                    self.tree.focus(item)
                    self.tree.see(item)  # Cuộn đến vị trí của dòng tìm thấy
                    return
            messagebox.showinfo("Thông báo", "Không tìm thấy kết quả nào.")
