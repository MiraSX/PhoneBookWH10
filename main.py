from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name] = record.phones

    def __str__(self):
        for name, phones in self.data.items():
            return f'{name}: {", ".join(str(phone) for phone in phones)}'


class Field:
    pass


class Name(Field):
    def __init__(self, name):
        if not name:
            raise ValueError(f'Name can\'t be empty!')
        else:
            self.name = name

    def __str__(self) -> str:
        return self.name


class Phone(Field):
    def __init__(self, phone):
        self.phone = phone

    def __str__(self) -> str:
        return self.phone


class Record:
    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone
        self.phones = []
        if phone:
            self.phones.append(phone)

    def add_phone(self, phone):
        self.phones.append(phone)

    def delete_phone(self, phone):
        self.phones.remove(phone)

    def change_phone(self, phone_old, phone_new):
        try:
            self.phones.remove(phone_old)
            self.phones.append(phone_new)
        except ValueError as e:
            return e


if __name__ == '__main__':
    ab = AddressBook()

    name1 = Name('Anton')
    phoneA1 = Phone('5435463')
    phoneA2 = Phone('4231423')
    rec1 = Record(name1, phoneA1)
    rec1.add_phone(phoneA2)
    phonechange1 = Phone('1111')
    rec1.delete_phone(phoneA2)
    rec1.change_phone(phoneA1, phonechange1)

    ab.add_record(rec1)
    print(ab)
