from collections import deque

d = deque()

while True:
    instruction, *value = input().split()
    if instruction == 'push_front':
        d.append(value[0])
        print('ok')
    if instruction == 'push_back':
        d.appendleft(value[0])
        print('ok')
    try:
        if instruction == 'pop_front':
            print(d.pop())
        if instruction == 'pop_back':
            print(d.popleft())
        if instruction == 'front':
            print(d[-1])
        if instruction == 'back':
            print(d[0])
    except IndexError:
        print('error')
    if instruction == 'size':
        print(len(d))
    if instruction == 'clear':
        d.clear()
        print('ok')
    if instruction == 'exit':
        print('bye')
        break
