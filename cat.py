input_file = open('input.txt', 'r')
input_lines = input_file.readlines()
input_file.close()

seq = ''

for line in input_lines:
    if line.startswith('>'):
        continue
    else:
        seq += line.strip()

counted_catalans = {'':1, 'A':0, 'C':0, 'G':0, 'U':0, 'AA':0, 'AC':0, 'AG':0, 'AU':1, 'CA':0, 'CC':0, 'CG':1, 'CU':0, 'GA':0, 'GC':1, 'GG':0, 'GU':0, 'UA':1, 'UC':0, 'UG':0, 'UU':0}

subseqs = [seq]

def catalan(mat):
    if (mat not in counted_catalans):
        if mat.count('C') != mat.count('G') or mat.count('A') != mat.count('U'):
            counted_catalans[mat] = 0
        else:
            counted_catalans[mat] = sum([catalan(mat[1:i]) * counted_catalans[mat[0] + mat[i]] * catalan(mat[i + 1:]) for i in range(1, len(mat), 2)])
    return counted_catalans[mat]
print(catalan(subseqs[0]) % 1000000)