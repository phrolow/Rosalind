input_file = open('input.txt', 'r')
input_lines = input_file.readlines()
input_file.close()

seq = ''

for line in input_lines:
    if line.startswith('>'):
        continue
    else:
        seq += line.strip()

counted_motzs = {}

subseqs = [seq]


def motz(mat):
    lib = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}

    if (len(mat) <= 1):
        return 1

    elif (mat in counted_motzs):
        return counted_motzs[mat]

    else:
        counted_motzs[mat] = motz(mat[1:])

        for i in range(1, len(mat)):
            if (mat[i] == lib[mat[0]]):
                counted_motzs[mat] = counted_motzs[mat] + motz(mat[1:i]) * motz(mat[i + 1:])

    return counted_motzs[mat]


print(motz(subseqs[0]) % 1000000)