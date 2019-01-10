input()
l = map(int, input().split())
h = int(input())

print(len([i for i in l if i >= h]) + 1)
