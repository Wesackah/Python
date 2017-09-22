def lezen():
    infile = open('kaartnummers.txt', 'r')
    content = infile.readlines()
    for regel in content:
        regel = regel.strip().split(', ')
        print('{1:15} heeft kaartnummer: {0:6}'.format(regel[0], regel[1]))
    infile.close()




lezen()
