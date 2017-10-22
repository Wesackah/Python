import xmltodict

xmlFile = open('stations.xml', 'r')
xmlDict = xmltodict.parse(xmlFile.read())
xmlFile.close()

print('Dit zijn de codes en types van de 4 stations:')
for station in xmlDict['Stations']['Station']:
    print('{} - {}'.format(station['Code'], station['Type']))

print('\nAlle stations met synoniemen:')
for station in xmlDict['Stations']['Station']:
    if station['Synoniemen'] != None:
        print('{}\n'.format(station['Synoniemen']))

print('De lange naam van elk station:')
for station in xmlDict['Stations']['Station']:
   print(station['Namen']['Lang'])
