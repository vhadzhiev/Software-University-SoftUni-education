def list_manipulator(numbers, action, position, *args):
    if action == 'add':
        if position == 'beginning':
            return [*args] + numbers
        elif position == 'end':
            return numbers + [*args]
    elif action == 'remove':
        if position == 'beginning':
            if args:
                num = [*args][0]
                return numbers[num:]
            return numbers[1:]
        elif position == 'end':
            if args:
                num = [*args][0]
                return numbers[:-num]
            return numbers[:-1]


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
