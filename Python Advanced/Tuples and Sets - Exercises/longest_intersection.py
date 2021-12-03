n = int(input())

longest_intersection = []
for _ in range(n):
    first_indices, second_indices = input().split('-')
    first_range = [int(x) for x in first_indices.split(',')]
    second_range = [int(x) for x in second_indices.split(',')]
    first_set = {x for x in range(first_range[0], first_range[1] + 1)}
    second_set = {x for x in range(second_range[0], second_range[1] + 1)}

    intersection = first_set.intersection(second_set)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

longest_intersection_str = ', '.join(str(x) for x in longest_intersection)
print(f'Longest intersection is [{longest_intersection_str}] with length {len(longest_intersection)}')
