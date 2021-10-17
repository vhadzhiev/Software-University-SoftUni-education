from collections import deque

male_stack = [int(x) for x in input().split()]
female_queue = deque(int(x) for x in input().split())

matches = 0
while male_stack and female_queue:
    male = male_stack.pop()
    female = female_queue.popleft()

    if male <= 0:
        female_queue.appendleft(female)
        continue
    if female <= 0:
        male_stack.append(male)
        continue
    if male % 25 == 0:
        if male_stack:
            male_stack.pop()
        female_queue.appendleft(female)
        continue
    if female % 25 == 0:
        if female_queue:
            female_queue.popleft()
        male_stack.append(male)
        continue

    if male == female:
        matches += 1
    else:
        male_stack.append(male - 2)

print(f'Matches: {matches}')
if male_stack:
    print(f"Males left: {', '.join(str(x) for x in male_stack[::-1])}")
else:
    print('Males left: none')
if female_queue:
    print(f"Females left: {', '.join(str(x) for x in female_queue)}")
else:
    print('Females left: none')
