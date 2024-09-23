import itertools


def lex_key(seq):
    res = 0
    deg = n
    for letter in seq:
        res += abc.index(letter) * (len(abc) ** deg)
        deg -= 1

    return res


abc = 'O A E Y D C X H I P'
abc = abc.replace(' ', '')
n = 3

seqs = []

for j in range(1, n + 1):
    for i in itertools.product(abc, repeat=j):
        seqs.append(''.join(i))

for i in sorted(seqs, key=lex_key):
    print(i)