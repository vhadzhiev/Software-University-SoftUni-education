parentheses = input()

opening_p_stack = []
balanced = True
for ch in parentheses:
    if ch in '([{':
        opening_p_stack.append(ch)
    else:
        if len(opening_p_stack) == 0:
            balanced = False
            break
        opening_symbol = opening_p_stack.pop()
        pair = f'{opening_symbol}{ch}'
        if pair not in '()[]{}':
            balanced = False
            break

if balanced and len(opening_p_stack) == 0:
    print('YES')
else:
    print('NO')
