stack = []

numcontainers = int(input())
_, *boxes = input().split()
stack += boxes
for container in range(1, numcontainers):
    _, *boxes = input().split()
    for box in boxes:
        print(container, 0)
        stack.append(box)

if set(stack) > numcontainers:
    print(0)
else:
    for box in range(1, numcontainers):

