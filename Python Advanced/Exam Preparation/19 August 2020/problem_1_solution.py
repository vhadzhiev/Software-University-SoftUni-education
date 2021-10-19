from collections import deque

customers_queue = deque(int(x) for x in input().split(', '))
taxis_stack = [int(x) for x in input().split(', ')]

total_time = 0
while customers_queue and taxis_stack:
    customer = customers_queue.popleft()
    taxi = taxis_stack.pop()

    if taxi >= customer:
        total_time += customer
    else:
        customers_queue.appendleft(customer)

if customers_queue:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join(str(x) for x in customers_queue)}')
else:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')