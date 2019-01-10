s = [1, 1]
n = int(input())

for i in range(n):
    s.append(s[-1] + s[-2])

print(' '.join(map(str, s[:n])))
