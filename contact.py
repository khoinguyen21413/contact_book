class Contact:
    def __init__(self,id, last_name, first_name, gender, phone, email, address):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.gender = gender
        self.phone = phone
        self.email = email
        self.address = address

    def to_tuple(self):
        """Trả về tuple để insert vào TreeView"""
        return (self.id, self.last_name, self.first_name, self.gender, self.phone, self.email, self.address)
