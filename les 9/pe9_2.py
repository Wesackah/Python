import datetime
import csv

while True:
    lijst = ['einde', 'Einde', ' einde', ' Einde', 'einde ', 'Einde ']
    naam = input("Wat is je achternaam? ")
    if naam in lijst:
        break
    else:
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")

with open('inloggers.csv', 'a', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow((naam, voorl, gbdatum, email))

