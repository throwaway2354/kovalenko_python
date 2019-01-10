input()
l = input().split()
shift = -(int(input()) % len(l))

print(' '.join(l[shift:] + l[:shift]))
