import itertools

quadromers_dict = {}

quadromers_keys = itertools.product('ACGT', repeat=4)
for i in quadromers_keys:
    q_str = ''.join(i)
    quadromers_dict[q_str] = 0

input_file = open('input.txt', 'r')
input_lines = input_file.readlines()
input_file.close()

seq = ''

for line in input_lines:
    if line.startswith('>'):
        continue
    else:
        seq += line.strip()

for i in range(len(seq) - 3):
    quadromers_dict[seq[i:i + 4]] += 1

for i in quadromers_dict.keys():
    print(quadromers_dict[i], end=' ')