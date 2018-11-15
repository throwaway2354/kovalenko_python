child_to_parent = {}

for _ in range(int(input()) - 1):
    child, parent = input().split()
    child_to_parent[child] = parent

for orig_name in sorted(
        set(child_to_parent.keys())
        | set(child_to_parent.values())):
    name = orig_name
    depth = 0
    while True:
        try:
            name = child_to_parent[name]
        except KeyError:
            print(orig_name, depth)
            break
        else:
            depth += 1
