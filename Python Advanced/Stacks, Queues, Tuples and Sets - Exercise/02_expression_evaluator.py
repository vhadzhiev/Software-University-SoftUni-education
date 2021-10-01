from collections import deque

string_expression = input().split()

numbers_queue = deque()
for x in string_expression:
    if x not in '+-*/':
        numbers_queue.append(int(x))
    else:
        result = 0
        if x == '-':
            while len(numbers_queue) > 1:
                result = numbers_queue.popleft() - numbers_queue.popleft()
                numbers_queue.appendleft(result)
        elif x == '+':
            while len(numbers_queue) > 1:
                result = numbers_queue.popleft() + numbers_queue.popleft()
                numbers_queue.appendleft(result)
        elif x == '*':
            while len(numbers_queue) > 1:
                result = numbers_queue.popleft() * numbers_queue.popleft()
                numbers_queue.appendleft(result)
        elif x == '/':
            while len(numbers_queue) > 1:
                result = numbers_queue.popleft() // numbers_queue.popleft()
                numbers_queue.appendleft(result)

print(numbers_queue.pop())
