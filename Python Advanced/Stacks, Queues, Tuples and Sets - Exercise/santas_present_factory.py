from collections import deque

materials_stack = [int(x) for x in input().split()]
magic_level_queue = deque([int(x) for x in input().split()])

presents = {
    'Doll': 0,
    'Wooden train': 0,
    'Teddy bear': 0,
    'Bicycle': 0
}

while materials_stack and magic_level_queue:
    material = materials_stack.pop()
    magic_level = magic_level_queue.popleft()
    magic = material * magic_level

    if material == 0 and magic_level == 0:
        continue
    if material == 0:
        magic_level_queue.appendleft(magic_level)
        continue
    if magic_level == 0:
        materials_stack.append(material)
        continue

    if magic < 0:
        materials_stack.append(material + magic_level)
    elif magic == 150:
        presents['Doll'] += 1
    elif magic == 250:
        presents['Wooden train'] += 1
    elif magic == 300:
        presents['Teddy bear'] += 1
    elif magic == 400:
        presents['Bicycle'] += 1
    else:
        materials_stack.append(material + 15)

if (presents['Doll'] > 0 and presents['Wooden train'] > 0) or (presents['Teddy bear'] > 0 and presents['Bicycle'] > 0):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials_stack:
    materials_stack_str = ', '.join(reversed([str(x) for x in materials_stack]))
    print(f'Materials left: {materials_stack_str}')
if magic_level_queue:
    magic_level_queue_str = ', '.join([str(x) for x in magic_level_queue])
    print(f'Magic left: {magic_level_queue_str}')
    
for present, count in sorted(presents.items()):
    if count > 0:
        print(f"{present}: {count}")
