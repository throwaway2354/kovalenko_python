from collections import deque

d = deque()

try:
    while True:
        try:
            instruction, *value = input().strip()
        except:
            break
        card = ''.join(value).strip()
        if instruction == '^':
            d.popleft()
        if instruction == '/':
            d.pop()
        if instruction == '+':
            d.appendleft(card)
        if instruction == '#':
            d.append(card)
except Exception:
    print('ERROR')
else:
    if not d:
        print('EMPTY')
    else:
        print(*d)
