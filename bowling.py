n, k = map(int, input().split())
s = ['I' for _ in range(n)]
for _ in range(k):
    l, r = map(int, input().split())
    l -= 1
    s = s[:l] + ['.'] * (r - l) + s[r:]
print(''.join(s))
