from collections import deque

chocolates_stack = [int(x) for x in input().split(', ')]
milk_queue = deque([int(x) for x in input().split(', ')])

milkshakes = 0
while chocolates_stack and milk_queue:
    if chocolates_stack[-1] <= 0:
        chocolates_stack.pop()
    if milk_queue[0] <= 0:
        milk_queue.popleft()

    if chocolates_stack and milk_queue:
        if chocolates_stack[-1] > 0 and milk_queue[0] > 0:
            if chocolates_stack[-1] == milk_queue[0]:
                chocolates_stack.pop()
                milk_queue.popleft()
                milkshakes += 1
            else:
                chocolates_stack[-1] -= 5
                milk_queue.append(milk_queue.popleft())

    if milkshakes == 5:
        break

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates_stack:
    chocolates_stack_str = ', '.join(str(x) for x in chocolates_stack)
    print(f"Chocolate: {chocolates_stack_str}")
else:
    print("Chocolate: empty")

if milk_queue:
    milk_queue_str = ', '.join(str(x) for x in milk_queue)
    print(f"Milk: {milk_queue_str}")
else:
    print("Milk: empty")
