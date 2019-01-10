d, m = map(int, input().split())

l = [0] * (m + 1)

for c in range(m, 0, -1):
    sequence_length = c
    j = 1
    prev_chain_length = 0
    while sequence_length <= m:
        l[sequence_length] = j
        prev_chain_length += d
        sequence_length += prev_chain_length
        j += 1
        print('    ', *l)
    print(*l)

print(*l)
