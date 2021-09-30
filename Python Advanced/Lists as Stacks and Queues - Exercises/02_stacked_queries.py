n = int(input())

numbers_stack = []
for _ in range(n):
    query = input()
    if query.startswith('1'):
        numbers = query.split()
        numbers_stack.append(int(numbers[1]))
    elif query.startswith('2') and numbers_stack:
        numbers_stack.pop()
    elif query.startswith('3') and numbers_stack:
        print(max(numbers_stack))
    elif query.startswith('4') and numbers_stack:
        print(min(numbers_stack))

numbers_stack_str = []
while numbers_stack:
    numbers_stack_str.append(str(numbers_stack.pop()))

print(', '.join(numbers_stack_str))
