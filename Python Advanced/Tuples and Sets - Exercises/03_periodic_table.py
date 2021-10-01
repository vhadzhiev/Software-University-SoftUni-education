n = int(input())

chemical_elements = set()
for _ in range(n):
    compound = input().split()
    for el in compound:
        chemical_elements.add(el)

[print(el) for el in chemical_elements]
