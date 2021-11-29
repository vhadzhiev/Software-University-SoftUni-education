from collections import deque

petrol_pumps = int(input())

pumps_queue = deque()
for _ in range(petrol_pumps):
    petrol_pump = [int(x) for x in input().split()]
    pumps_queue.append(petrol_pump)

for index in range(petrol_pumps):
    fuel = 0
    completed = True
    for pump in pumps_queue:
        litres = pump[0]
        distance = pump[1]
        fuel += litres
        if fuel < distance:
            completed = False
            break
        fuel -= distance
    if completed:
        print(index)
        break
    else:
        pumps_queue.append(pumps_queue.popleft())
