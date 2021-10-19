def numbers_searching(*args):
    numbers = sorted([*args])
    smallest_number = min(numbers)
    biggest_number = max(numbers)
    missing_number = None
    duplicates = []
    for number in numbers:
        if numbers.count(number) > 1 and number not in duplicates:
            duplicates.append(number)
    for number in range(biggest_number, smallest_number, - 1):
        if number not in numbers:
            missing_number = number
            break

    return [missing_number, duplicates]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))