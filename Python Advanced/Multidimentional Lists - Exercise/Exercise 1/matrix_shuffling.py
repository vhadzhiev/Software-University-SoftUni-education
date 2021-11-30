def valid_index(matrix, ind1, ind2, ind3, ind4):
    return 0 <= ind1 < len(matrix) and 0 <= ind2 < len(matrix[0]) and 0 <= ind3 < len(matrix) and 0 <= ind4 < len(
        matrix[0])


rows, columns = [int(x) for x in input().split()]

matrix = []
for _ in range(rows):
    matrix.append([x for x in input().split()])

while True:
    command = input()
    if command == 'END':
        break

    command = command.split()

    if 'swap' not in command or len(command) != 5:
        print('Invalid input!')
    else:
        ind1, ind2, ind3, ind4 = int(command[1]), int(command[2]), int(command[3]), int(command[4])
        if not valid_index(matrix, ind1, ind2, ind3, ind4):
            print('Invalid input!')
        else:
            matrix[ind1][ind2], matrix[ind3][ind4] = matrix[ind3][ind4], matrix[ind1][ind2]
            for row in range(len(matrix)):
                print(' '.join(x for x in matrix[row]))
