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


presents_count = int(input())
size = int(input())

matrix = []
santa_row = 0
santa_col = 0
nice_kids = 0
nice_kids_with_gifts = 0
for row in range(size):
    elements = input().split()
    matrix.append(elements)
    for col in range(size):
        element = elements[col]
        if element == 'S':
            santa_row, santa_col = row, col
        elif element == 'V':
            nice_kids += 1

while True:
    command = input()

    if command == 'Christmas morning':
        break

    new_r, new_c = get_next_position(command, santa_row, santa_col)
    if is_valid(size, new_r, new_c):
        matrix[santa_row][santa_col] = '-'
        santa_row, santa_col = new_r, new_c
        if matrix[santa_row][santa_col] == 'V':
            presents_count -= 1
            nice_kids_with_gifts += 1
        elif matrix[santa_row][santa_col] == 'C':
            if matrix[santa_row - 1][santa_col] == 'V':
                presents_count -= 1
                nice_kids_with_gifts += 1
            if matrix[santa_row - 1][santa_col] == 'X':
                presents_count -= 1
            matrix[santa_row - 1][santa_col] = '-'
            if matrix[santa_row + 1][santa_col] == 'V':
                presents_count -= 1
                nice_kids_with_gifts += 1
            if matrix[santa_row + 1][santa_col] == 'X':
                presents_count -= 1
            matrix[santa_row + 1][santa_col] = '-'
            if matrix[santa_row][santa_col - 1] == 'V':
                presents_count -= 1
                nice_kids_with_gifts += 1
            if matrix[santa_row][santa_col - 1] == 'X':
                presents_count -= 1
            matrix[santa_row][santa_col - 1] = '-'
            if matrix[santa_row][santa_col + 1] == 'V':
                presents_count -= 1
                nice_kids_with_gifts += 1
            if matrix[santa_row][santa_col + 1] == 'X':
                presents_count -= 1
            matrix[santa_row][santa_col + 1] = '-'

        matrix[santa_row][santa_col] = 'S'

        if presents_count <= 0:
            break

if presents_count == 0 and nice_kids > nice_kids_with_gifts:
    print("Santa ran out of presents!")
for row in matrix:
    print(' '.join(row))
if nice_kids_with_gifts >= nice_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - nice_kids_with_gifts} nice kid/s.")
