def reverse_complement(seq):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    revc = ''
    for i in seq:
        revc += complement[i]
    revc = revc[::-1]
    return revc


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

del input_lines

true_seqs = set()
errs = set()

for seq in seqs:
    rev_comp = reverse_complement(seq)

    if seq in errs:
        errs.remove(seq)

        true_seqs.add(rev_comp)
        true_seqs.add(seq)
    if rev_comp in errs:
        errs.remove(rev_comp)

        true_seqs.add(rev_comp)
        true_seqs.add(seq)
    if not ((seq in true_seqs) or (rev_comp in true_seqs)):
        errs.add(seq)

for err in errs:
    for seq in true_seqs:
        if sum(ech != sch for ech, sch in zip(err, seq)) == 1:
            print('%s->%s' % (err, seq))