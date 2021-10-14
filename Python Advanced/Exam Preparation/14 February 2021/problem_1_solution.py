from collections import deque

firework_effects = deque(int(x) for x in input().split(', '))
explosive_powers = [int(x) for x in input().split(', ')]

palm = 0
willow = 0
crossette = 0
while firework_effects and explosive_powers:
    effect = firework_effects.popleft()
    power = explosive_powers.pop()

    if effect <= 0:
        explosive_powers.append(power)
        continue
    if power <= 0:
        firework_effects.appendleft(effect)
        continue

    mix = power + effect
    if mix % 3 == 0 and mix % 5 == 0:
        crossette += 1
    elif mix % 3 == 0:
        palm += 1
    elif mix % 5 == 0:
        willow += 1
    else:
        firework_effects.append(effect - 1)
        explosive_powers.append(power)

    if palm >= 3 and willow >= 3 and crossette >= 3:
        print('Congrats! You made the perfect firework show!')
        break

if palm < 3 or willow < 3 or crossette < 3:
    print("Sorry. You can't make the perfect firework show.")
if firework_effects:
    firework_effects_str = ', '.join(str(x) for x in firework_effects)
    print(f'Firework Effects left: {firework_effects_str}')
if explosive_powers:
    explosive_powers_str = ', '.join(str(x) for x in explosive_powers)
    print(f'Explosive Power left: {explosive_powers_str}')
print(f'Palm Fireworks: {palm}')
print(f'Willow Fireworks: {willow}')
print(f'Crossette Fireworks: {crossette}')
