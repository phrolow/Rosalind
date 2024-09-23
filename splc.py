import re

input_file = open('input.txt', 'r')
input_lines = input_file.readlines()
input_file.close()

seqs = []

for line in input_lines:
    if not line.startswith(">"):
        seqs[-1] = seqs[-1] + line.strip()
    if line.startswith(">"):
        seqs.append('')

dna_seq = seqs[0]
seqs.pop(0)

for seq in seqs:
    dna_seq = dna_seq.replace(seq, '')

table_file = open('dna_table.txt', 'r')
table_content = table_file.read()
table_file.close()

table_splitted = re.split('\\s+', table_content)
dna_dict = {}

for i in range(0, len(table_splitted), 2):
    dna_dict[table_splitted[i]] = table_splitted[i + 1]

prot = ''
for j in range(0, len(dna_seq) - 2, 3):
    aa = dna_dict[dna_seq[j:j + 3]]
    if aa == 'Stop':
        print(prot)
        break
    prot += aa