import csv
lstnaam = []
lstdatum = []
lstscore = []
with open('kol.csv', 'r') as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter=';')
    for row in reader:
        lstnaam.append(row[0])
        lstdatum.append(row[1])
        lstscore.append(row[2])
    x = max(lstscore)
    y = lstscore.index(x)
    print("Hoogste score is {}, op {} behaald door {}. ".format(x, lstdatum[y], lstnaam[y]))
