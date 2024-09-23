n_seqs = 81733
gc_content = 0.436286
seq = 'CTACAAAT'

proba_dict = {'A' : (1 - gc_content) / 2, 'C' : gc_content / 2, 'G' : gc_content / 2, 'T' : (1 - gc_content) / 2}

proba = 1

for i in seq:
    proba *= proba_dict[i]

print(1 - (1 - proba) ** n_seqs)