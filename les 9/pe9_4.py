import csv
# Artikelnummer = input('Artikelnummer')
# Artikelcode = input('Artikelcode')
# Naam=input('')
# Voorraad
# Prijs
# with open('inloggers.csv', 'a', newline='') as myCSVFile:
#     writer = csv.writer(myCSVFile, delimiter=';')
#     writer.writerow(())
#
lstArtikelnummer = []
lstArtikelcode = []
lstNaam=[]
lstVoorraad=[]
lstPrijs=[]

with open('kol2.csv', 'r') as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter=';')
    next(reader)
    for row in reader:
        lstArtikelnummer.append(eval(row[0]))
        lstArtikelcode.append(row[1])
        lstNaam.append(row[2])
        lstVoorraad.append(eval(row[3]))
        lstPrijs.append(eval(row[4]))

    y = lstPrijs.index(max(lstPrijs))

print(' Het duurste artikel is de {}, deze kost {} Euro \n Er zijn {} exemplaren in voorraad met productnummer {}\n In totaal zijn er {} artikelen.'.format(lstNaam[y], max(lstPrijs), lstVoorraad[y], lstArtikelnummer[y], sum(lstVoorraad)))