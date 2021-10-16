from collections import deque

pizza_orders = deque(int(x) for x in input().split(', '))
employee_capacity = [int(x) for x in input().split(', ')]

pizzas_made = 0
while pizza_orders and employee_capacity:
    order = pizza_orders.popleft()
    employee = employee_capacity.pop()

    if order <= 0 or order > 10:
        employee_capacity.append(employee)
        continue

    if order <= employee:
        pizzas_made += order
    else:
        pizzas_made += employee
        pizza_orders.appendleft(order - employee)

if not pizza_orders:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {pizzas_made}')
    print(f'Employees: {", ".join(str(x) for x in employee_capacity)}')
else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join(str(x) for x in pizza_orders)}')
