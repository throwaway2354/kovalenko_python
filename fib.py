with open('input.txt') as fin, open('output.txt', 'w') as fout:
    s = [0, 1]
    n = int(fin.readline())
    for i in range(n):
        s.append(s[-1] + s[-2])
    fout.write(' '.join(map(str, s[:n])))

