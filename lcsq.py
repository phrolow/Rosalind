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

seq1 = seqs[0]
seq2 = seqs[1]


def longest_subseq(X, Y):
    m = len(X)
    n = len(Y)

    L = [[None] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = ''
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + X[i - 1]
            else:
                if len(L[i - 1][j]) > len(L[i][j - 1]):
                    L[i][j] = L[i - 1][j]
                else:
                    L[i][j] = L[i][j - 1]
    return L[m][n]


longest_subseq(seq1, seq2)