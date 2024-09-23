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

edit_dist = [[i] * len(seqs[0]) for i in range(len(seqs[1]))]

for i in range(len(seqs[0])):
    edit_dist[0][i] = i

for i in range(1, len(seqs[1])):
    for j in range(1, len(seqs[0])):
        edit_dist[i][j] = min(edit_dist[i - 1][j] + 1, edit_dist[i][j - 1] + 1,
                              edit_dist[i - 1][j - 1] + int(seqs[1][i - 1] != seqs[0][j - 1]))

print(edit_dist[i][j])