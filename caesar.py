import string

alphabet = string.ascii_lowercase
shifted_alphabet = alphabet[3:] + alphabet[:3]
table = str.maketrans(alphabet, shifted_alphabet)

with open('input.txt') as fin, open('output.txt', 'w') as fout:
    line = fin.readline()
    fout.write(line.translate(table))
