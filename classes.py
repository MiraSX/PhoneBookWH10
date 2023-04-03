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
        return str(self.name)


class Phone(Field):
    def __init__(self, phone):
        self.phone = phone

    def __repr__(self):
        return str(self.phone)


class Record:
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phone = phone
        self.phones = []
        if phone:
            self.add_phone(phone)

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def change_phone(self, phone_old: Phone, phone_new: Phone):
        index = self.__check_phone(phone_old)
        if index >= 0:
            self.phones.pop(index)
            self.phones.insert(index, phone_new)
            return f"Phone {phone_old.phone} success change to phone {phone_new.phone}"
        return f'Phone {phone_old.phone} dos not in phones'

    def delete_phone(self, phone: Phone):
        index = self.__check_phone(phone)
        if index >= 0:
            self.phones.pop(index)
            return f'Phone {phone.phone} was deleted'
        return f'Phone {phone.phone} dos not in phones'

    def __check_phone(self, phone: Phone) -> int | None:
        for i, p in enumerate(self.phones):
            if p.phone == phone.phone:
                return i
        return None

    def __repr__(self) -> str:
        return f"{', '.join([p.phone for p in self.phones])}"


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.name] = record


if __name__ == '__main__':
    ab = AddressBook()

    name1 = Name('Anton')
    phoneA1 = Phone('1234')
    phoneA2 = Phone('1111')
    rec1 = Record(name1, phoneA1)
    ab.add_record(rec1)

    print(ab)

    phoneA3 = Phone('1234')

    print(rec1.change_phone(phoneA3, phoneA2))

    print(ab[name1.name])
    print(ab[name1.name].phones)

    for rec in ab.values():
        print(rec.phones)
    print(ab)
    print(rec1.delete_phone(phoneA2))
    print(ab)
