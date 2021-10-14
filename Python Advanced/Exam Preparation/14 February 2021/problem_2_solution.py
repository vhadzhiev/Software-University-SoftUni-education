def get_next_position(direction, r, c):
    if direction == 'up':
        return r - 1, c
    elif direction == 'down':
        return r + 1, c
    elif direction == 'left':
        return r, c - 1
    elif direction == 'right':
        return r, c + 1


def is_valid(size, r, c):
    return 0 <= r < size and 0 <= c < size


size = int(input())

matrix = []
player_r = 0
player_c = 0
for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)
    for col in range(len(row_elements)):
        if row_elements[col] == 'P':
            player_r = row
            player_c = col

coins = 0
path = []
directions = ["up", "down", "left", "right"]
while True:
    direction = input()

    if direction not in directions:
        continue

    new_r, new_c = get_next_position(direction, player_r, player_c)
    if not is_valid(size, new_r, new_c) or matrix[new_r][new_c] == 'X':
        print(f"Game over! You've collected {coins // 2} coins.")
        break

    coins += int(matrix[new_r][new_c])
    path.append([new_r, new_c])
    player_r = new_r
    player_c = new_c
    if coins >= 100:
        print(f"You won! You've collected {coins} coins.")
        break

print('Your path:')
for x in path:
    print(x)
