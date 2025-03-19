import sqlite3

DB_NAME = "contacts.db"

def create_db():
    # Kết nối hoặc tạo mới database "contacts.db"
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()

    # Tạo bảng Contacts nếu chưa tồn tại
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            last_name TEXT NOT NULL,
            first_name TEXT NOT NULL,
            gender TEXT CHECK(gender IN ('Nam', 'Nữ')) NOT NULL,
            phone TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            address TEXT
        )
    """)

    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

def get_all_contacts():
    """Lấy tất cả liên hệ từ database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Contacts")
    contacts = cursor.fetchall()
    conn.close()
    return contacts

def add_contact(contact):
    """Thêm liên hệ mới vào database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Contacts (id,last_name, first_name, gender, phone, email, address) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (contact.id, contact.last_name, contact.first_name, contact.gender, contact.phone, contact.email, contact.address))
    conn.commit()
    conn.close()


def get_contact_count():
    """Trả về số lượng contact trong database."""
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM Contacts")
    count = cursor.fetchone()[0]  # Lấy giá trị đếm
    
    conn.close()
    return count