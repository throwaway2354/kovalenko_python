from collections import defaultdict

record = defaultdict(int)
while True:
    try:
        candidate, votes = input().split()
    except:
        break
    record[candidate] += int(votes)

for key, value in sorted(record.items()):
    print(key, value)
