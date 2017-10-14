lijst = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 's-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal']
def inlezen_beginstation(stations):
    while True:
        invoer = input('geef beginstation ')
        if invoer in stations:
            return invoer
            break
        else:
            print(f' Deze trein komt niet in {invoer}')



def inlezen_eindstation(stations, beginstation):
    while True:
        invoer2 = input('geef eindstation')
        if invoer2 in stations:
           if stations.index(invoer2) > stations.index(beginstation):
                return invoer2
                break
           else:
               print('fout2')
        else:
            print('fout3')

def omroepen_reis(stations, beginstation, eindstation):
        indexbegin = stations.index(beginstation) + 1
        indexeind = stations.index(eindstation) + 1
        verschil = indexeind - indexbegin
        print(f'Het beginstation {beginstation} is het {indexbegin}e op het traject')
        print(f'Het eindstation {eindstation} is het {indexeind}e op het traject')
        print(f'U reist {verschil} stations, dit kost {verschil*5} euro.')

invoer = inlezen_beginstation(lijst)
invoer2 = inlezen_eindstation(lijst, invoer)
omroepen_reis(lijst, invoer, invoer2)