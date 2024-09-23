input_file = open('input.txt', 'r')
input_lines = input_file.readlines()
input_file.close()

n = int(input_lines[0].strip())
set0 = set([i for i in range(1, n+1)])
set1 = set(list(map(int, input_lines[1].strip()[1:-1].replace(',', '').split())))
set2 = set(list(map(int, input_lines[2].strip()[1:-1].replace(',', '').split())))

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))
print(set0.difference(set1))
print(set0.difference(set2))
