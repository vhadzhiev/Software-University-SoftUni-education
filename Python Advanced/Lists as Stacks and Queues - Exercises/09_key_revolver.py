from collections import deque

bullet_price = int(input())
gun_barrel = int(input())
bullets_stack = [int(x) for x in input().split()]
locks = [int(x) for x in input().split()]
intelligence_value = int(input())

locks_queue = deque([x for x in locks])
bullets_shot = 0
bullets_cost = 0
while bullets_stack and locks_queue:
    if bullets_stack.pop() <= locks_queue[0]:
        locks_queue.popleft()
        print('Bang!')
    else:
        print('Ping!')
    bullets_shot += 1
    bullets_cost += bullet_price
    if bullets_shot >= gun_barrel and bullets_stack:
        bullets_shot = 0
        print('Reloading!')

if not bullets_stack and locks_queue:
    print(f"Couldn't get through. Locks left: {len(locks_queue)}")
if not locks_queue:
    print(f"{len(bullets_stack)} bullets left. Earned ${intelligence_value - bullets_cost}")
