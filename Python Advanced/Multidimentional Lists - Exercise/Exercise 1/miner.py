def is_command_valid(size: int, new_r: int, new_c: int):
    return 0 <= new_r < size and 0 <= new_c < size


def get_next_position(direction: str, r: int, c: int):
    if direction == 'up':
        return r - 1, c
    elif direction == 'down':
        return r + 1, c
    elif direction == 'left':
        return r, c - 1
    else:
        return r, c + 1


size = int(input())
commands = input().split()

matrix = []
r = 0
c = 0
for row in range(size):
    row_elements = [x for x in input().split()]
    matrix.append(row_elements)
    for col in range(size):
        if row_elements[col] == 's':
            r = row
            c = col

coal = [x for row in matrix for x in row].count('c')
position = matrix[r][c]
more_coal = True
for direction in commands:
    new_r, new_c = get_next_position(direction, r, c)

    if is_command_valid(size, new_r, new_c):
        r = new_r
        c = new_c

    if matrix[r][c] == 'e':
        print(f"Game over! ({r}, {c})")
        more_coal = False
        break
    elif matrix[r][c] == 'c':
        matrix[r][c] = '*'
        coal -= 1
        if coal == 0:
            print(f"You collected all coal! ({r}, {c})")
            more_coal = False
            break

if more_coal:
    print(f"{coal} pieces of coal left. ({r}, {c})")
