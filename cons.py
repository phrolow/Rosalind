f = open('input.txt', 'r')

txt = f.read()
txt = txt.replace('\n', '')
lines = txt.split('>')

for i in range(len(lines)):
    lines[i] = lines[i][13:]

lines.pop(0)

line_len = len(lines[0])

a = [0] * line_len
c = [0] * line_len
g = [0] * line_len
t = [0] * line_len

for line in lines:
    if line[0] == '>':
        continue

    for i in range(len(line)):
        if line[i] == 'A':
            a[i] += 1
        elif line[i] == 'C':
            c[i] += 1
        elif line[i] == 'G':
            g[i] += 1
        elif line[i] == 'T':
            t[i] += 1

f.close()

res = [0] * line_len

for i in range(line_len):
    if (a[i] >= c[i]) and (a[i] >= g[i]) and (a[i] >= t[i]):
        res[i] = 'A'
    elif (c[i] >= g[i]) and (c[i] >= t[i]) and (c[i] >= a[i]):
        res[i] = 'C'
    elif (g[i] >= c[i]) and (g[i] >= t[i]) and (g[i] >= a[i]):
        res[i] = 'G'
    elif (t[i] >= c[i]) and (t[i] >= a[i]) and (t[i] >= g[i]):
        res[i] = 'T'

print("".join(res))
print('A:', *a)
print('C:', *c)
print('G:', *g)
print('T:', *t)