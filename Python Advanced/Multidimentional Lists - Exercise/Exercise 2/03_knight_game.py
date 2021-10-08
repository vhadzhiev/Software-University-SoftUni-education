def knight_is_in_place(board, row, col):
    board_size = len(board)
    if not 0 <= row < board_size or not 0 <= col < board_size:
        return False
    return board[row][col] == 'K'


def count_hit_knights(board, row, col):
    result = 0
    if knight_is_in_place(board, row - 2, col - 1):
        result += 1
    if knight_is_in_place(board, row - 2, col + 1):
        result += 1
    if knight_is_in_place(board, row + 2, col - 1):
        result += 1
    if knight_is_in_place(board, row + 2, col + 1):
        result += 1
    if knight_is_in_place(board, row - 1, col - 2):
        result += 1
    if knight_is_in_place(board, row - 1, col + 2):
        result += 1
    if knight_is_in_place(board, row + 1, col - 2):
        result += 1
    if knight_is_in_place(board, row + 1, col + 2):
        result += 1
    return result


size = int(input())

matrix = []
for _ in range(size):
    matrix.append(list(input()))

removed_knights = 0
while True:
    max_count = 0
    knight_r = 0
    knight_c = 0

    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'K':
                count = count_hit_knights(matrix, r, c)
                if count > max_count:
                    max_count = count
                    knight_r = r
                    knight_c = c
    if max_count == 0:
        break
    matrix[knight_r][knight_c] = '0'
    removed_knights += 1

print(removed_knights)
