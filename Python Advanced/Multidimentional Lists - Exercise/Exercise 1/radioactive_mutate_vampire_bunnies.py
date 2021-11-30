def is_inside(rows, columns, r, c):
    return 0 <= r < rows and 0 <= c < columns


def get_next_position(direction, row, columns):
    if direction == 'U':
        return row - 1, columns
    if direction == 'D':
        return row + 1, columns
    if direction == 'L':
        return row, columns - 1
    if direction == 'R':
        return row, columns + 1


def get_new_bunnies(bunnies, rows, columns):
    new_bunnies = []
    for r, c in bunnies:
        if is_inside(rows, columns, r - 1, c):
            new_bunnies.append([r - 1, c])
        if is_inside(rows, columns, r + 1, c):
            new_bunnies.append([r + 1, c])
        if is_inside(rows, columns, r, c - 1):
            new_bunnies.append([r, c - 1])
        if is_inside(rows, columns, r, c + 1):
            new_bunnies.append([r, c + 1])
    return new_bunnies


rows, columns = [int(x) for x in input().split()]

matrix = []
player_r = 0
player_c = 0
bunnies = []
for row in range(rows):
    row_elements = list(input())
    matrix.append(row_elements)
    for col in range(columns):
        x = row_elements[col]
        if x == 'P':
            player_r = row
            player_c = col
        elif x == 'B':
            bunnies.append([row, col])

commands = input()

matrix[player_r][player_c] = '.'
won = None
for command in commands:
    new_r, new_c = get_next_position(command, player_r, player_c)
    if not is_inside(rows, columns, new_r, new_c):
        won = True
    elif matrix[new_r][new_c] == 'B':
        won = False

    if not won:
        player_r = new_r
        player_c = new_c

    new_bunnies = get_new_bunnies(bunnies, rows, columns)
    for r, c in new_bunnies:
        if r == player_r and c == player_c and not won:
            won = False
        matrix[r][c] = 'B'
    bunnies = new_bunnies
    if won is not None:
        break

for row_elements in matrix:
    print(''.join(row_elements))
if won:
    print(f'won: {player_r} {player_c}')
else:
    print(f'dead: {player_r} {player_c}')
