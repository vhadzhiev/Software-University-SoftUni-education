def is_valid(size, r, c):
    return 0 <= r < size and 0 <= c < size


def get_next_position(direction, r, c, steps):
    if direction == 'up':
        return r - steps, c
    if direction == 'down':
        return r + steps, c
    if direction == 'left':
        return r, c - steps
    return r, c + steps


size = 5
matrix = []
starting_r = 0
starting_c = 0
targets = 0
shot_targets = []
for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)
    for col in range(size):
        element = row_elements[col]
        if element == 'A':
            starting_r = row
            starting_c = col
        elif element == 'x':
            targets += 1

r = starting_r
c = starting_c
n = int(input())
for _ in range(n):
    command = input().split()
    action = command[0]
    direction = command[1]

    if action == 'move':
        steps = int(command[2])
        new_r, new_c = get_next_position(direction, r, c, steps)
        if is_valid(size, new_r, new_c) and matrix[new_r][new_c] == '.':
            matrix[r][c] = '.'
            matrix[new_r][new_c] = 'A'
            r, c = new_r, new_c
    elif action == 'shoot':
        bullet_r, bullet_c = get_next_position(direction, r, c, 1)
        while is_valid(size, bullet_r, bullet_c):
            if matrix[bullet_r][bullet_c] == 'x':
                targets -= 1
                shot_targets.append([bullet_r, bullet_c])
                matrix[bullet_r][bullet_c] = '.'
                break
            bullet_r, bullet_c = get_next_position(direction, bullet_r, bullet_c, 1)

    if targets == 0:
        break

if targets > 0:
    print(f'Training not completed! {targets} targets left.')
else:
    print(f'Training completed! All {len(shot_targets)} targets hit.')
for x in shot_targets:
    print(x)
