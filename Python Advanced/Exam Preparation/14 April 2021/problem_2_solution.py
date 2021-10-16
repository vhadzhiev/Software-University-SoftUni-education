def is_valid(size, r, c):
    return 0 <= r < size and 0 <= c < size


def get_player_points(matrix, r, c):
    if not is_valid(board_size, row, col):
        return 0
    elif matrix[r][c] == 'B':
        return 501
    elif matrix[r][c] == 'T':
        return 3 * (int(matrix[r][0]) + int(matrix[r][-1]) + int(matrix[0][c]) + int(matrix[-1][c]))
    elif matrix[r][c] == 'D':
        return 2 * (int(matrix[r][0]) + int(matrix[r][-1]) + int(matrix[0][c]) + int(matrix[-1][c]))
    else:
        return int(matrix[r][c])


player1, player2 = input().split(', ')

player_points = {player1: 501, player2: 501}
board_size = 7
board = []
for _ in range(board_size):
    board.append(input().split())

turns = 0
won = False
while True:
    turns += 1
    for player in player_points.keys():
        coordinates = input()
        row, col = int(coordinates[1]), int(coordinates[-2])

        points = get_player_points(board, row, col)
        player_points[player] -= points
        if player_points[player] <= 0:
            print(f"{player} won the game with {turns} throws!")
            won = True
            break

    if won:
        break
