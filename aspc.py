import math

n = 1793
m = 1302

res = 0

for k in range(m, n + 1):
    res += math.comb(n, k)
    res %= 1000000

print(res)
