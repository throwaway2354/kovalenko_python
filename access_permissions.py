from collections import defaultdict


def default_value():
    return [False, False, False]


files = defaultdict(default_value)


def check_perms(action, perms):
    if action == 'read' and not perms[0]:
        return False
    if action == 'write' and not perms[1]:
        return False
    if action == 'execute' and not perms[2]:
        return False
    return True


for _ in range(int(input())):
    name, *perms = input().split()
    if 'R' in perms:
        files[name][0] = True
    if 'W' in perms:
        files[name][1] = True
    if 'X' in perms:
        files[name][2] = True

for _ in range(int(input())):
    action, name = input().split()
    if check_perms(action, files[name]):
        print('OK')
    else:
        print('Access denied')
