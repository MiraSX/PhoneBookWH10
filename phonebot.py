from classes import AddressBook, Record, Name, Phone


def input_error(func):
    def inner(*args, contacts):
        try:
            return func(*args, contacts)
        except (KeyError, ValueError, IndexError) as e:
            return e
    return inner


def hello(*args, **kwargs):
    return 'How can I help you?'


@input_error
def add(name, number, contacts):
    name_user = Name(name)
    phone_number = Phone(number)

    if name_user.name not in contacts:
        contacts[name_user.name] = Record(name_user, phone_number)
    else:
        contacts[name_user.name].add_phone(phone_number)

    return (f'User {name_user.name} with {phone_number} phone number was added')


@input_error
def change(name, old, new, contacts):
    name_user = Name(name)
    old_number = Phone(old)
    new_number = Phone(new)

    if name_user.name not in contacts:
        return (f'There is no {name_user.name}')
    else:
        contacts[name_user.name].change_phone(
            old_number, new_number)
        return (f'{name_user.name} number was changed from {old_number} to {new_number}')


@input_error
def phone(name, contacts):
    user_name = Name(name)
    if user_name.name in contacts:
        return (f'{user_name.name}\'s number is {contacts[user_name.name]}')
    else:
        return (f'There is no {user_name.name}')


@input_error
def delete(name, phone, contacts):
    user_name = Name(name)
    phone_number = Phone(phone)

    if user_name.name in contacts:
        contacts[user_name.name].delete_phone(phone_number)
        return f'{user_name.name}\'s phone - {phone_number} was deleted'
    else:
        return (f'There is no {user_name.name}')


def show_all(*args, contacts):
    return ('\n'.join([f'{name}: {contacts[name]}' for name in contacts]))


def main():
    contacts = AddressBook()

    while True:

        inp_command = input('Enter command: ').lower().split()
        if not inp_command:
            continue

        if inp_command[0] == "good bye" or inp_command[0] == "close" or inp_command[0] == "exit":
            break

        COMMANDS = {'hello': hello,
                    'add': add,
                    'change': change,
                    'phone': phone,
                    'show': show_all,
                    'delete': delete}

        if inp_command[0] in COMMANDS:
            handler = COMMANDS[inp_command[0]]
            print(handler(*inp_command[1:], contacts=contacts))
        else:
            print('Unknown command')
            continue


if __name__ == '__main__':
    main()
