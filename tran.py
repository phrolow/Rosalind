f = open('input.txt', 'r')
lines = f.readlines()
f.close()

seqs = []

for line_index in range(len(lines)):
    lines[line_index] = lines[line_index].strip()
    if lines[line_index].startswith('>'):
        seqs.append('')
    else:
        seqs[-1] += lines[line_index]

transi = 0
transv = 0

for i, j in zip(seqs[0], seqs[1]):
    if i == j:
        continue
    if (i == 'A' and j == 'T') or (i == 'T' and j == 'A') or (i == 'C' and j == 'G') or (i == 'G' and j == 'C') or (
            i == 'A' and j == 'C') or (i == 'C' and j == 'A') or (i == 'G' and j == 'T') or (i == 'T' and j == 'G'):
        transv += 1
    else:
        transi += 1

print(f'{(transi / transv):.11f}')