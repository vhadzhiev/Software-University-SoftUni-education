first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())
n = int(input())

for _ in range(n):
    command, sequence, *third_set = input().split()
    if command == 'Add':
        if sequence == 'First':
            [first_set.add(int(x)) for x in third_set]
        else:
            [second_set.add(int(x)) for x in third_set]
    elif command == 'Remove':
        if sequence == 'First':
            first_set.difference_update({int(x) for x in third_set})
        else:
            second_set.difference_update({int(x) for x in third_set})
    else:
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print(True)
        else:
            print(False)

print(', '.join([str(x) for x in sorted(first_set)]))
print(', '.join([str(x) for x in sorted(second_set)]))
