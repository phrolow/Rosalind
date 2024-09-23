import math

input_file = open('input.txt', 'r')
input_lines = input_file.readlines()
input_file.close()

seqs = []

for line in input_lines:
    if line.startswith('>'):
        seqs.append('')
        continue
    else:
        seqs[-1] += line.strip()

seq = seqs[0]

num_A = seq.count('A')
num_C = seq.count('C')
num_G = seq.count('G')
num_U = seq.count('U')

num_AU = math.perm(max(num_A, num_U), min(num_A, num_U))
num_CG = math.perm(max(num_C, num_G), min(num_C, num_G))

num_AU * num_CG