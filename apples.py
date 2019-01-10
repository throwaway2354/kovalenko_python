with open('input.txt') as fin, open('output.txt', 'w') as fout:
    s = list(map(int, fin.readline().split()))[:3]
    ss = sorted(s)
    if s[0] == s[1] == s[2]:
        fout.write('0')
    elif (ss[0] + ss[2]) / 2 != s[1]:
        fout.write('-1')
    else:
        fout.write(f'{s.index(ss[2]) + 1} {s.index(ss[0]) + 1} {ss[2] - ss[1]}')
