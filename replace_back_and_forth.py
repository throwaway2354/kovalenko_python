s1 = input()
s2 = (
    s1
    .replace('a', '1')
    .replace('A', '2')
    .replace('b', 'a')
    .replace('B', 'A')
    .replace('1', 'b')
    .replace('2', 'B')
)

print(s2)
print(sum(1 for t in zip(s1, s2) if t[0] != t[1]))
