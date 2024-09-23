def hamming_distance(s1, s2):
    dist = 0

    for i, j in zip(s1, s2):
        if i != j:
            dist += 1

    return dist


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

for i in seqs:
    for j in seqs:
        print(hamming_distance(i, j) / len(i), end=' ')
    print('')