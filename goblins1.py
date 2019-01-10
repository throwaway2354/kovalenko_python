from collections import deque

d = deque()

for _ in range(int(input())):
    line = input()
    if line == '-':
        print(d.pop())
    else:
        privilege, id_number = line.split()
        if privilege == '+':
            d.appendleft(id_number)
        else:
            d.insert(len(d) // 2, id_number)
