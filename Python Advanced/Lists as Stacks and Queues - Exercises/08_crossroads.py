from collections import deque

green_light = int(input())
yellow_light = int(input())

cars_queue = deque()
cars_passed = 0
while True:
    command = input()
    if command == 'END':
        print("Everyone is safe.")
        print(f"{cars_passed} total cars passed the crossroads.")
        break
    elif command == 'green':
        green = green_light
        car = ''
        while green > 0 and cars_queue:
            car = cars_queue.popleft()
            green -= len(car)
            cars_passed += 1
        if green <= 0:
            if len(car) > green + yellow_light:
                cars_passed -= 1
                print("A crash happened!")
                print(f"{car} was hit at {car[green + yellow_light]}.")
                break
    else:
        cars_queue.append(command)
