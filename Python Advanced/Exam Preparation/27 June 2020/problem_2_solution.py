def get_next_position(direction, matrix, r, c):
    if direction == 'up':
        return r - 1, c
    elif direction == 'down':
        return r + 1, c
    elif direction == 'left':
        return r, c - 1
    else:
        return r, c + 1


def is_valid(size, r, c):
    return 0 <= r < size and 0 <= c < size


size = int(input())

field = []
snake_r = 0
snake_c = 0
burrows = []
food = 0
for row in range(size):
    row_elements = [x for x in input()]
    field.append(row_elements)
    for col in range(len(row_elements)):
        if row_elements[col] == 'S':
            snake_r = row
            snake_c = col
        elif row_elements[col] == 'B':
            burrows.append([row, col])

while True:
    direction = input()
    new_r, new_c = get_next_position(direction, field, snake_r, snake_c)
    if not is_valid(size, new_r, new_c):
        field[snake_r][snake_c] = '.'
        print('Game over!')
        break
    elif field[new_r][new_c] == 'B':
        field[new_r][new_c] = '.'
        burrows.remove([new_r, new_c])
        new_r, new_c = burrows[0]
    elif field[new_r][new_c] == '*':
        food += 1

    field[snake_r][snake_c] = '.'
    field[new_r][new_c] = 'S'
    snake_r, snake_c = new_r, new_c

    if food == 10:
        print('You won! You fed the snake.')
        break

print(f'Food eaten: {food}')
for row in field:
    print(''.join(row))

