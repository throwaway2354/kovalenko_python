from itertools import chain


orig_colors = colors = list(map(int, input().split()))


def cluster(colors):
    prev_color = None
    count = 0
    for color in colors:
        if color == prev_color:
            count += 1
        else:
            yield [prev_color] * count
            count = 1
            prev_color = color
    yield [prev_color] * count


prev_len = len(orig_colors)
while True:
    colors = list(chain.from_iterable(
        sequence
        for sequence in
        cluster(colors)
        if len(sequence) < 3
    ))
    if len(colors) == prev_len:
        break
    prev_len = len(colors)

print(len(orig_colors) - len(colors))
