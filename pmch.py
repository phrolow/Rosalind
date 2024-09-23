seq = 'AAGGACCCGUCUACACAGUGGGAGUUAGCGCCAGCUCUGAUUUGAUACAGCAAAGUUCGUAAGUCGUCUGUCGCCCUA'

num_a = seq.count('A')
au_pairs = 1
for i in range(1, num_a + 1):
    au_pairs *= i

num_c = seq.count('C')
cg_pairs = 1
for i in range(1, num_c + 1):
    cg_pairs *= i

print(num_a, num_c)
print(au_pairs * cg_pairs)