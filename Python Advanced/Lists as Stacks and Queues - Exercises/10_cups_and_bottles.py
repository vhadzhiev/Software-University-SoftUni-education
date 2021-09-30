from collections import deque

cups_queue = deque([int(x) for x in input().split()])
bottles_stack = [int(x) for x in input().split()]

wasted_water = 0
while cups_queue and bottles_stack:
    cup = cups_queue[0]
    while cup > 0 and bottles_stack:
        bottle = bottles_stack.pop()
        cup -= bottle
        if cup <= 0:
            wasted_water += abs(cup)
            cups_queue.popleft()

if bottles_stack:
    bottles = [str(x) for x in bottles_stack]
    print(f"Bottles: {' '.join(bottles[::-1])}")
if cups_queue:
    cups = [str(x) for x in cups_queue]
    print(f"Cups: {' '.join(cups)}")
print(f'Wasted litters of water: {wasted_water}')
