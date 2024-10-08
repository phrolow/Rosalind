import re

table_file = open('aa_mass.txt', 'r')
table_content = table_file.read()
table_file.close()

table_splitted = re.split('\\s+', table_content)
aa_mass = {}

for i in range(0, len(table_splitted) - 1, 2):
    aa_mass[table_splitted[i]] = float(table_splitted[i + 1])

weight = .0

prot = 'WVPPQSDGTTCLRLWCIQWSDMEYYPYRQLDAIYNRKFLDLRAMMVNCQVFGFSSKQWVDANMWCSQFMIRKYINGDVCCFHYSPSFKGTAYYMKIATYRHLHSSKLEVGIFSMTHPRCGDDIFLPLYTITEPEHYYIWDRWTEANKINDLLEWLHVEHCMMTQGWWLFDFKYPGISTMRQNPNVHVAFSYPVQQTCYMNTRQASVMAYGEDEQKHVCLYSPNHISSPRSLGCEEHNSDISHNNCRNYNWCYKICFFSCCIQNYAPMTEAVALVVQCQGHTANHWGICPYLTKQAMCNEPINKHCIHIMELWSVMERTPTGSAWCFRPTVMFQTWHDVDYQYWQWDEMHSNTIFPKNFGNFSFERKWPYWLNYKHPCARSAILEFSSYKAMIPYWLMKQIQSTINFPQDHSAGLLKKFHVMTFIDFITLKMYQSRTYHLISFGNHMTYNMFIQQFNKEGPAAPEDRMQKGATSMKCRWSNAMCYLHLMIEHHSSFMMKKFETVQCPWVSWTVTEYGHWYPGPESPIHITENPKSFQFNQCFMPCDEWFLDEADADHSAAVSLSDVHMINPLDAMQWNVAEYYCPFAHGQMTDMQHYSDSCEYQKGSMFIPGRQDDAHYKSKVSNWHAAWTRQFADTSHSVKMGRWHEEDQHNNESGAHPFSGPNLHMAPKDEHRDWTLFDWNDGGEIHAIQMIYTWVFRAWTVKEKKNAFKMHNEMCACSLHPVGDACMPMSQIDPGGALNDFGLEDPKKRWRGTPKRVPLNSLDFKYCYMSPKFHICSWYTNDIIAYMSAADCTKQLIYHWNNAVSIFRGGYNSNFMYSTTNHQQRFYNVKKEFPVGYHEKAINHMIPICYTTHKHWWCTGMEVIVFCLHECISLPHDKLIEFLYYDGLCESEMFGVVNRTYSTGYLDRVFIAKNFAIWSMIWASMDGARGESPGKAALSKASAVINLPKYDKMSRDSNAYNRIIWGWITYARITSPDTRQEHPP'
for i in prot:
    weight += aa_mass[i]

print(f'{weight:9.3f}')