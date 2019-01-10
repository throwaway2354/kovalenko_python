with open('input.txt') as fin, open('output.txt', 'w') as fout:
    fout.write(str(sum(map(int, fin.readline().split()))))
