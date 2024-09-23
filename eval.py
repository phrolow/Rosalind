n = 967122
seq = 'ATTCACGC'
gcs_line = '0.000 0.068 0.144 0.193 0.264 0.349 0.393 0.414 0.495 0.562 0.623 0.698 0.743 0.806 0.851 0.893 1.000'
gcs = gcs_line.split(' ')

for gc in gcs:
    probas = {}
    gc = float(gc)
    probas['A'] = (1 - gc) / 2
    probas['C'] = gc / 2
    probas['G'] = gc / 2
    probas['T'] = (1 - gc) / 2

    seq_proba = 1
    for base in seq:
        seq_proba *= probas[base]

    print(seq_proba * (n + 1 - len(seq)), end=' ')