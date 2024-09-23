def long_substr(data):
  substrs = lambda x: {x[i:i+j] for i in range(len(x)) for j in range(len(x) - i + 1)}
  s = substrs(data[0])
  for val in data[1:]:
    s.intersection_update(substrs(val))
  return max(s, key=len)

f = open('input.txt', 'r')

lines = f.readlines()
seqs = []
last = -1

for line_index in range(len(lines)):
    lines[line_index] = lines[line_index].strip()
    if lines[line_index].startswith('>'):
        seqs.append('')
        last += 1
    else:
        seqs[last] += lines[line_index]

f.close()

print(seqs)

print(long_substr(seqs))