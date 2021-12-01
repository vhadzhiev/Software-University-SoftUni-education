def is_valid(size, r, c):
    return 0 <= r < size and 0 <= c < size


size = int(input())

matrix = []
for _ in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    command = input().split()

    if command[0] == 'END':
        break
    elif command[0] == 'Add':
        r = int(command[1])
        c = int(command[2])
        value = int(command[3])
        if is_valid(size, r, c):
            matrix[r][c] += value
        else:
            print('Invalid coordinates')
    elif command[0] == 'Subtract':
        r = int(command[1])
        c = int(command[2])
        value = int(command[3])
        if is_valid(size, r, c):
            matrix[r][c] -= value
        else:
            print('Invalid coordinates')

for i in range(size):
    print(' '.join(str(x) for x in matrix[i]))
