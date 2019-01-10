with open('input.txt') as fin, open('output.txt', 'w') as fout:
    line = fin.readline().strip()
    letter = fin.readline().strip()
    if 'abc' not in line:
        if letter != 'c':
            fout.write(line + letter)
        else:
            fout.write(letter + line)
    else:
        index = line.index('abc')
        if letter != 'c':
            line = line[:index + 2] + letter + line[index + 2:]
        else:
            line = line[:index + 1] + letter + line[index + 1:]
    fout.write(line)
