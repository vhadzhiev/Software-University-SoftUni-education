from collections import deque

food_quantity = int(input())
orders = input().split()

orders_queue = deque()
for order in orders:
    orders_queue.appendleft(int(order))

print(max(orders_queue))

while orders_queue:
    if orders_queue[-1] <= food_quantity:
        food_quantity -= orders_queue.pop()
    else:
        break

if not orders_queue:
    print('Orders complete')
else:
    print(f'Orders left: ', end='')
    while orders_queue:
        print(orders_queue.pop(), end=' ')