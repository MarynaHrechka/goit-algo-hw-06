import re
from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
		pass


class Phone(Field):

    def __init__(self, value):
        if len(value) != 10:
            raise ValueError
        pattern = r'\d{10}'
        digits = re.findall(pattern, value)
        if not digits:
            raise ValueError
        super().__init__(digits[0])


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        item = Phone(phone)
        self.phones.append(item)

    def remove_phone(self, phone: str):
        phones_copy = self.phones.copy()
        for item in phones_copy:
            if item.value == phone:
                   self.phones.remove(item)
    
    def edit_phone(self, old_phone: str, new_phone: str):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)
           
    def find_phone(self, phone: str):
        res = ''
        for item in self.phones:
            if item.value == phone:
                   res = phone
        return res
            

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    
    def add_record(self, record: Record):
        self.data[record.name.value] = record
    
    def delete(self, name: str):
        self.data.pop(name)
    
    def find(self, name: str):
        return self.data[name]
