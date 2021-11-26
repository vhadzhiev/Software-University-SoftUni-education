import os

while True:
    command = input()

    if command == 'End':
        break

    command_args = command.split('-')
    action = command_args[0]
    file_name = command_args[1]

    if action == 'Create':
        with open(file_name, 'w') as f:
            continue
    elif action == 'Add':
        content = command_args[2]
        with open(file_name, 'a') as f:
            f.write(f'{content}\n')
    elif action == 'Replace':
        old_string = command_args[2]
        new_string = command_args[3]
        words = []
        try:
            with open(file_name) as f:
                words = f.read().split()
                for i in range(len(words)):
                    if words[i] == old_string:
                        words[i] = new_string
        except FileNotFoundError:
            print("An error occurred")
            continue
        with open(file_name, 'w') as f:
            f.write(' '.join(words))
    elif action == 'Delete':
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")
