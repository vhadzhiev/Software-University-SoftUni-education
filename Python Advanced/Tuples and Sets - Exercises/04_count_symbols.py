text = input()

characters = {}
for ch in text:
    if ch not in characters:
        characters[ch] = 0
    characters[ch] += 1

for ch, count in sorted(characters.items(), key=lambda x: x[0]):
    print(f'{ch}: {count} time/s')
