from collections import deque

d = deque()
s = set()

with open('output.txt', 'w') as f, open('input.txt', 'r') as fin:
    try:
        for line in fin:
            instruction, *value = line.strip()
            card = ''.join(value)
            if instruction == '^':
                card = d.popleft()
                s.remove(card)
                continue
            if instruction == '/':
                card = d.pop()
                s.remove(card)
                continue
            if card in s:
                raise Exception()
            s.add(card)
            if instruction == '+':
                d.appendleft(card)
                continue
            if instruction == '#':
                d.append(card)
                continue
            raise Exception()
    except Exception:
        f.write('ERROR')
    else:
        if not d:
            f.write('EMPTY')
        else:
            f.write(' '.join(d))
