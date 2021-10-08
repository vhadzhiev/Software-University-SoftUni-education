def is_valid(size, r, c):
    return 0 <= r < size and 0 <= c < size


def get_next_position(direction, r, c):
    if direction == 'up':
        return r - 1, c
    if direction == 'down':
        return r + 1, c
    if direction == 'left':
        return r, c - 1
    return r, c + 1


size = int(input())

matrix = []
bunny_r = 0
bunny_c = 0
for row in range(size):
    elements = input().split()
    matrix.append(elements)
    for col in range(size):
        element = elements[col]
        if element == 'B':
            bunny_r = row
            bunny_c = col

eggs = float('-inf')
best_direction = ''
best_path = []
directions = ['right', 'left', 'up', 'down']
for direction in directions:
    current_eggs = 0
    path = []
    r = bunny_r
    c = bunny_c

    while True:
        next_r, next_c = get_next_position(direction, r, c)
        if not is_valid(size, next_r, next_c):
            break
        if matrix[next_r][next_c] == 'X':
            break
        else:
            current_eggs += int(matrix[next_r][next_c])
            path.append([next_r, next_c])
            r, c = next_r, next_c

    if current_eggs > eggs:
        eggs = current_eggs
        best_direction = direction
        best_path = path

print(best_direction)
for x in best_path:
    print(x)
print(eggs)
