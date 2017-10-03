vraag = input('geef filenaam op: ')
dic = {}
def lezen(filenaam):
    infile = open(filenaam, 'r')
    content = infile.readlines()
    for regel in content:
        regel = regel.strip().split(':')
        bedrijf = regel[0]
        sym = regel[1]
        dic[sym] = bedrijf

    return dic

a = lezen(vraag)

j = input('geef bedrijf op')
for k,v in a.items():
    if j == k:
        print(k)
    elif j == v:
        print(v)