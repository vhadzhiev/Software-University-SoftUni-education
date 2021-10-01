n, m = [int(x) for x in input().split()]

first_set = {input() for x in range(n)}
second_set = {input() for x in range(m)}

same_elements = first_set.intersection(second_set)
[print(el) for el in same_elements]
