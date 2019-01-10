from itertools import product

letters = input()
length = int(input())

words = list(product(letters, repeat=length))

for word in words:
    print(''.join(word))
print(len(words))
