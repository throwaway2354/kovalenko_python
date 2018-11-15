from collections import defaultdict

d = defaultdict(list)

for _ in range(int(input())):
    english, stuff = input().split(' - ')
    latin = stuff.split(', ')
    for word in latin:
        d[word].append(english)

print(len(d))
for word, translations in sorted(d.items()):
    print(f'{word} - {", ".join(translations)}')
