import itertools

n = 4
signed_perms = []
total = 0
perms = itertools.permutations(list(range(1, n + 1)))

for i in perms:
    signs = itertools.product([-1, 1], repeat = len(list(range(1, n + 1))))
    for j in signs:
        e = [i * sign for i, sign in zip(i, j)]
        signed_perms.append(e)
        total = total + 1

print(total)

for i in range(0, len(signed_perms)):
    print(*signed_perms[i], sep=' ')
