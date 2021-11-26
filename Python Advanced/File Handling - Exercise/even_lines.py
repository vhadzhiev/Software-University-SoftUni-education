characters_set = {"-", ",", ".", "!", "?"}
lines = []
with open('text.txt') as f:
    for line in f:
        modified_line = ''
        for i in range(len(line)):
            if line[i] not in characters_set:
                modified_line += line[i]
            else:
                modified_line += '@'
        lines.append(modified_line)

for i in range(len(lines)):
    if i % 2 == 0:
        line = lines[i].split()
        print(' '.join(x for x in line[::-1]))
