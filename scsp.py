input_file = open('input.txt', 'r')
input_lines = input_file.readlines()
input_file.close()

seq1 = input_lines[0].strip()
seq2 = input_lines[1].strip()


def longest_subseq(X, Y):
    m = len(X)
    n = len(Y)

    L = [[''] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                L[i][j] = Y[:j]
            elif j == 0:
                L[i][j] = X[:i]
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + X[i - 1]
            else:
                if len(L[i - 1][j]) < len(L[i][j - 1]):
                    L[i][j] = L[i - 1][j] + X[i - 1]
                else:
                    L[i][j] = L[i][j - 1] + Y[j - 1]
    return L[m][n]


longest_subseq(seq1, seq2)