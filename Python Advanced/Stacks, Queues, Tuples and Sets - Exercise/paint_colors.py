from collections import deque

substrings = deque(input().split())

main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}

crafted_colors = []
while substrings:
    left = substrings.popleft()
    right = substrings.pop() if substrings else ''
    color = left + right
    if color in main_colors or color in secondary_colors:
        crafted_colors.append(color)
        continue
    color = right + left
    if color in main_colors or color in secondary_colors:
        crafted_colors.append(color)
        continue
    else:
        left = left[:-1]
        right = right[:-1]
        index = len(substrings) // 2
        if left:
            substrings.insert(index, left)
        if right:
            substrings.insert(index, right)

secondary_from_main_colors = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['blue', 'yellow']
}

for color in crafted_colors:
    if color in main_colors:
        continue
    required_colors = set(secondary_from_main_colors[color])
    if not required_colors.issubset(crafted_colors):
        crafted_colors.remove(color)

print(crafted_colors)
