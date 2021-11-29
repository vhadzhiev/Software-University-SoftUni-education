clothes_stack = input().split()
rack_capacity = int(input())

racks = 1
current_rack = 0

while clothes_stack:
    new_clothes = int(clothes_stack.pop())
    if current_rack + new_clothes <= rack_capacity:
        current_rack += new_clothes
    else:
        racks += 1
        current_rack = new_clothes

print(racks)
