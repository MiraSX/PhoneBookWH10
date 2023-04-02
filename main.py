from collections import UserDict


class Field:
    pass


class Name(Field):
    def __init__(self, name):
        if not name:
            raise ValueError(f'Name can\'t be empty!')
        else:
            self.name = name

    def __str__(self):
        return self.name


class Phone(Field):
    def __init__(self, phone):
        self.phone = phone

    def __str__(self):
        return self.phone


class Record:
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phone = phone
        self.phones = []
        if phone:
            self.phones.append(str(phone))

    def add_phone(self, phone):
        self.phones.append(str(phone))

    def delete_phone(self, phone):
        self.phones.remove(str(phone))

    def change_phone(self, phone_old, phone_new):
        try:
            self.phones.remove(str(phone_old))
            self.phones.append(str(phone_new))
        except ValueError as e:
            return e


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.name] = record


if __name__ == '__main__':
    ab = AddressBook()

    name1 = Name('Anton')
    phoneA1 = Phone('5435463')
    phoneA2 = Phone('4231423')
    rec1 = Record(name1, phoneA1)
    rec1.add_phone(phoneA2)
    ab.add_record(rec1)
    print(ab[name1.name])
    print(ab[name1.name].phones)

    for rec in ab.values():
        print(rec.phones)
    print(ab)
