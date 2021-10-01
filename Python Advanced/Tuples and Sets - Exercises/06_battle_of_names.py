n = int(input())

odd_set = set()
even_set = set()
for row in range(1, n + 1):
    name = input()
    name_value = 0
    for ch in name:
        name_value += ord(ch)

    devised_name_value = name_value // row
    if devised_name_value % 2 == 0:
        even_set.add(devised_name_value)
    else:
        odd_set.add(devised_name_value)

odd_sum = sum(odd_set)
even_sum = sum(even_set)
if odd_sum == even_sum:
    intersection = odd_set.intersection(even_set)
    intersection_str = ', '.join(str(x) for x in intersection)
    print(intersection_str)
elif odd_sum > even_sum:
    difference = odd_set.difference(even_set)
    difference_str = ', '.join(str(x) for x in difference)
    print(difference_str)
else:
    symmetric_difference = odd_set.symmetric_difference(even_set)
    symmetric_difference_str = ', '.join(str(x) for x in symmetric_difference)
    print(symmetric_difference_str)
