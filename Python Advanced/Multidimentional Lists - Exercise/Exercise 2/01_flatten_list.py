list_to_flatten = input().split('|')

result = []
for inside_list in list_to_flatten[::-1]:
    result += inside_list.split()

print(' '.join(result))
