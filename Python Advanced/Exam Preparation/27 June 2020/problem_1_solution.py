from collections import deque

bomb_effects = deque(int(x) for x in input().split(', '))
bomb_casings = [int(x) for x in input().split(', ')]

datura = 0
cherry = 0
smoke = 0
while bomb_effects and bomb_casings:
    effect = bomb_effects.popleft()
    casing = bomb_casings.pop()

    mix = effect + casing

    if mix == 40:
        datura += 1
    elif mix == 60:
        cherry += 1
    elif mix == 120:
        smoke += 1
    else:
        bomb_effects.appendleft(effect)
        bomb_casings.append(casing - 5)

    if datura >= 3 and cherry >= 3 and smoke >= 3:
        break

if datura >= 3 and cherry >= 3 and smoke >= 3:
    print('Bene! You have successfully filled the bomb pouch!')
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f'Bomb Effects: {", ".join(str(x) for x in bomb_effects)}')
else:
    print('Bomb Effects: empty')

if bomb_casings:
    print(f'Bomb Casings: {", ".join(str(x) for x in bomb_casings)}')
else:
    print('Bomb Casings: empty')

print(f"Cherry Bombs: {cherry}")
print(f"Datura Bombs: {datura}")
print(f"Smoke Decoy Bombs: {smoke}")
