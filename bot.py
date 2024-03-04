CONTACTS = {}


def input_error(func):
    def inner(*args):

        try:
            return func(*args)
        except IndexError:
            return 'Not enough params'
        except KeyError:
            return 'You have no contact with that name'
        except ValueError:
            return 'Give me name and phone please'

    return inner


def hello(*args):
    return 'How can I help you?'


@input_error
def add(*args):
    information = args[0]
    if information[0] not in CONTACTS:
        CONTACTS[information[0]] = information[1]
        return f'A contact with the name {information[0]} and number: {information[1]} has been added'
    else:
        return 'A contact with the same name already exists'


@input_error
def change(*args):
    information = args[0]
    if information[0] in CONTACTS:
        CONTACTS[information[0]] = information[1]
        return f'The {information[0]} contact number has been changed to: {information[1]}'
    else:
        raise KeyError


@input_error
def phone(*args):
    information = args[0]
    return CONTACTS[information[0]]


@input_error
def show_all(*args):
    all_contacts = ''
    for name, phone in CONTACTS.items():
        all_contacts += f'{name}: {phone}\n'

    return all_contacts.strip()


def close(*args):
    return 'Good bye!'


def no_command(*args):
    return 'Unknown command'


COMMANDS = {
    hello: ['hello'],
    add: ['add'],
    change: ['change'],
    phone: ['phone'],
    show_all: ['show all', 'show'],
    close: ['good bye', 'close', 'exit', '.', 'good']

}


@input_error
def get_handler(command):

    for func, k_words in COMMANDS.items():
        for word in k_words:
            if command.startswith(word):
                return func

    return no_command


def main():

    while True:

        user_input = input('>>> ')

        if not user_input:
            continue

        input_list = user_input.split()

        command = input_list[0].lower()
        data = input_list[1:]

        function = get_handler(command)
        print(function(data))

        if function.__name__ == 'close':
            break


if __name__ == '__main__':
    main()
