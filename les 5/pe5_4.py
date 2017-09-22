def lezen():
    infile = open('kaartnummers.txt', 'r')
    content = infile.readlines()
    print(content)
    infile.close()

