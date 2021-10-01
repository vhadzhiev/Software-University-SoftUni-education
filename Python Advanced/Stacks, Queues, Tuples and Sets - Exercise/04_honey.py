from collections import deque

working_bees_queue = deque([int(x) for x in input().split()])
nectar_stack = ([int(x) for x in input().split()])
symbols_queue = deque([x for x in input().split()])

total_honey = 0
while working_bees_queue and nectar_stack:
    bee = working_bees_queue[0]
    nectar = nectar_stack.pop()
    if nectar >= bee:
        symbol = symbols_queue.popleft()
        if symbol == '+':
            total_honey += bee + nectar
        elif symbol == '-':
            total_honey += abs(bee - nectar)
        elif symbol == '*':
            total_honey += bee * nectar
        elif symbol == '/' and not nectar == 0:
            total_honey += bee / nectar
        working_bees_queue.popleft()

print(f"Total honey made: {total_honey}")
if working_bees_queue:
    print(f'Bees left: {", ".join(str(x) for x in working_bees_queue)}')
if nectar_stack:
    print(f'Nectar left: {", ".join(str(x) for x in nectar_stack)}')
