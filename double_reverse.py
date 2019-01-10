n, a, b, c, d = map(int, input().split())

a -= 1
c -= 1

l = list(range(1, n + 1))

l = l[:a] + l[a:b][::-1] + l[b:]
l = l[:c] + l[c:d][::-1] + l[d:]

print(' '.join(map(str, l)))
