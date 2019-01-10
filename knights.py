with open('input.txt') as fin, open('output.txt', 'w') as fout:
    l = list(map(int, fin.readline().split()))
    s1 = l[0], l[1]
    s2 = l[2], l[3]
    if ((max([s1[0], s2[0]]) - 1 == min([s1[0], s2[0]])
            and max([s1[1], s2[1]]) - 2 == min([s1[1], s2[1]]))
            or (
                max([s1[0], s2[0]]) - 2 == min([s1[0], s2[0]])
                and max([s1[1], s2[1]]) - 1 == min([s1[1], s2[1]]))):
        fout.write('yes')
    else:
        fout.write('no')

