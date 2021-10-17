def get_next_position(direction, r, c):
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


string = input()
size = int(input())

field = []
player_r = 0
player_c = 0
for row in range(size):
    row_elements = [x for x in input()]
    field.append(row_elements)
    for col in range(len(row_elements)):
        if row_elements[col] == 'P':
            player_r = row
            player_c = col

count = int(input())
for _ in range(count):
    direction = input()
    new_r, new_c = get_next_position(direction, player_r, player_c)
    if not is_valid(size, new_r, new_c):
        string = string[:-1]
        continue

    if field[new_r][new_c].isalpha():
        string += field[new_r][new_c]

    field[player_r][player_c] = '-'
    field[new_r][new_c] = 'P'
    player_r, player_c = new_r, new_c

print(string)
for row in field:
    print(''.join(row))
