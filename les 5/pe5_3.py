def lezen():
    infile = open('kaartnummers.txt', 'r')
    content = infile.readlines()
    for regel in content:
        regel = regel.strip().split(', ')
        print((regel[0]))

    infile.close()
lezen()