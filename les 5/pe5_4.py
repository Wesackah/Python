import datetime

def strftime():
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%a %d %b %Y, %X,")
    return s

while True:
    renner = input('Wat is je naam?')
    outfile = open('hardlopen.txt', 'a')
    outfile.write(strftime(),)
    outfile.write(renner + '\n')

    a = input('Wil je nog een renner toevoegen? Ja of nee?')
    lst_ja = ['ja', 'JA', 'jA', 'y']
    if a not in lst_ja:
        print('doei')
        break