def dis_tree(T, x, y):
    x_index = T.find(x)
    y_index = T.find(y)
    t = [i for i in T[min(x_index, y_index):max(x_index, y_index)] if i in [')', '(', ',']]
    bracket = ''
    for i in t:
        bracket += i
    while ',,' in bracket:
        bracket = bracket.replace(',,', ',')
    while '(,)' in bracket:
        bracket = bracket.replace('(,)', '')
    if bracket.count('(') == len(bracket):
        return len(bracket)
    elif bracket.count(')') == len(bracket):
        return len(bracket)
    elif bracket.count(',') == len(bracket):
        return 2
    else:
        return bracket.count(')') + bracket.count('(') + 2


with open('input.txt', 'r') as f:
    tree = [line.strip().replace(';', '') for line in f.readlines() if len(line.strip()) > 0]
for i in range(0, len(tree), 2):
    T = tree[i]
    x, y = tree[i + 1].split(' ')
    print(dis_tree(T, x, y), end=" ")
