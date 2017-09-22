def lezen():
    infile = open('kaartnummers.txt', 'r')
    content = infile.readlines()
    count = 0
    lst = []
    for regel in content:
        regel = regel.strip().split(', ')
        lst.append(int(regel[0]))
        count = count + 1
    print(f'deze file telt {count} regels')
    print(f'het hoogste getal is {max(lst)}, op regel {int(lst.index(max(lst))+1)}')
    infile.close()
lezen()