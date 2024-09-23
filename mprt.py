import re
import urllib.request

file = open('input.txt', 'r')
prots = file.readlines()
file.close()

pattern = "(?=N[^P][ST][^P])"

for prot in prots:
    prot = prot.strip()
    url = "https://rest.uniprot.org/uniprotkb/" + prot.split('_')[0] + ".fasta"

    page = urllib.request.urlopen(url)
    req_lines = page.readlines()
    req = ""

    for line in req_lines:
        line = str(line)

        if line[2] == '>':
            continue

        req += line.strip()[2:-3]

    if re.search(pattern, req) is None:
        continue

    print(prot)

    for match in re.finditer(pattern, req, re.VERBOSE):
        print(match.start() + 1, end=" ")

    print('\n')