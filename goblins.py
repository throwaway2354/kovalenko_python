from collections import deque

d1 = deque()
d2 = deque()

for _ in range(int(input())):
    line = input()
    while not (len(d1) == len(d2) or len(d1) == len(d2) + 1):
        if len(d1) < len(d2):
            d1.appendleft(d2.pop())
        elif len(d1) > len(d2):
            d2.append(d1.popleft())

    if line == '-':
        print(d1.pop())
    else:
        privilege, id_number = line.split()
        if privilege == '+':
            d2.appendleft(id_number)
        else:
            d1.appendleft(id_number)
