n = 914
res = 1

for i in range(n):
    res *= 2
    if res > 10 ** 8:
        res %= 10 ** 6

res % 10 ** 6
