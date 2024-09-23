import re

table_file = open('rna_table.txt', 'r')
table_content = table_file.read()
table_file.close()

table_splitted = re.split('\\s+', table_content)
rna_n_codons = {}

for i in range(1, len(table_splitted), 2):
    rna_n_codons[table_splitted[i]] = rna_n_codons.get(table_splitted[i], 0) + 1

input_file = open('input.txt', 'r')
prot = input_file.read()
input_file.close()

prot = prot.replace('\n', '')

res = rna_n_codons['Stop']

for i in prot:
    res *= rna_n_codons[i]
    if res > 1e8:
        res %= 1e6
    if i == 'Stop':
        break

print(res)