def odd_or_even(command, *args):
    result = None
    if command == 'Odd':
        result = sum([x for x in args if x % 2 != 0]) * len(args)
    else:
        result = sum([x for x in args if x % 2 == 0]) * len(args)
    return result


command = input()
numbers = [int(x) for x in input().split()]

print(odd_or_even(command, *numbers))