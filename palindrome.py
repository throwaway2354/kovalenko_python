s = input().replace(' ', '')

if s == ''.join(reversed(s)):
    print('YES')
else:
    print('NO')
