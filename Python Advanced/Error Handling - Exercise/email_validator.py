class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


while True:
    command = input()

    if command == 'End':
        break

    if '@' not in command:
        raise MustContainAtSymbolError('Email must contain @')
    else:
        username, mail = command.split('@')
        if len(username) <= 4:
            raise NameTooShortError('Name must be more than 4 characters')
        else:
            domain = mail.split('.')[-1]
            if domain not in ['bg', 'com', 'org', 'net']:
                raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')
            else:
                print('Email is valid')
