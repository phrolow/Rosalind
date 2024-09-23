import math

s = 'GGCAGTACCAGAGATCCGGCCTCTAGCGGGCACTCACAGGCCGAGAGTCTATTCTTCTGACAGGATAACACTTAATCCCTGATCCT'
A_line = '0.100 0.156 0.169 0.234 0.301 0.386 0.443 0.465 0.523 0.590 0.662 0.685 0.776 0.782 0.869 0.942'
A = []

for i in A_line.split(' '):
    A.append(float(i))

na_prob = {}

for i in A:
    res = 1

    na_prob['A'] = (1 - i) / 2
    na_prob['C'] = i / 2
    na_prob['G'] = i / 2
    na_prob['T'] = (1 - i) / 2

    for j in s:
        res *= na_prob[j]

    res = math.log(res, 10)
    print(f'{res:.3f}', end=' ')
