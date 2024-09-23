f = open('input.txt', 'r')

lines = f.readlines()
seqs = {}
last_new = 0

for i in range(len(lines)):
    lines[i] = lines[i].strip()
    if lines[i].startswith('>'):
        lines[i] = (lines[i])[1:]
        seqs[lines[i]] = ''
        last_new = i
    else:
        seqs[lines[last_new]] += lines[i]

k = 3

for seq in seqs:
    for seq2 in seqs:
        if seq == seq2:
            continue
        if (seqs[seq])[-k:] == (seqs[seq2])[:k]:
            print(seq, seq2)

f.close()