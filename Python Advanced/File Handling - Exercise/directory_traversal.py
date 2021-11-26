import os

result = {}
for _, _, files in os.walk(input()):
    for file in files:
        ext = file.split('.')[-1]
        if ext not in result:
            result[ext] = []
        result[ext].append(file)
    break

with open(os.path.expanduser('~/Desktop/report.txt'), 'w') as output_file:
    for ext, files in sorted(result.items()):
        output_file.write(f'.{ext}\n')
        for file in files:
            output_file.write(f'---{file}\n')
