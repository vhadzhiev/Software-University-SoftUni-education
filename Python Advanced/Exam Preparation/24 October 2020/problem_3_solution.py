def best_list_pureness(*args):
    pureness = 0
    rotations = 0
    numbers_list = args[0]
    n = args[1]
    for rotation in range(n+1):
        total = 0
        for i in range(len(numbers_list)):
            total += numbers_list[i] * i
        if total > pureness:
            pureness = total
            rotations = rotation
        numbers_list.insert(0, numbers_list[-1])
        numbers_list.pop(-1)

    return f'Best pureness {pureness} after {rotations} rotations'
