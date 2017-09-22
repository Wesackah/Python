def standaardprijs(afstandKM):
     if afstandKM > 50:
        kost = 15 + afstandKM*.6
        return kost
     elif afstandKM <= 0:
            kost = 0
            return kost
     else:
            kost = afstandKM*.8
            return kost

def ritprijs(leeftijd, weekendrit, afstandKM):
    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit == True:
            return standaardprijs(afstandKM)*.65
        else:
            return standaardprijs(afstandKM)*.7
    else:
        if weekendrit == True:
            return  standaardprijs(afstandKM)*.6
        else:
            return standaardprijs(afstandKM)

x = eval(input('Aantal km gereisd?'))
y = input('is het weekend?')
z = eval(input('Wat is je leeftijd?'))
p = ['ja', 'Ja', 'JA', 'jA']
if y in p:
    print(ritprijs(z,True,x))
else:
    print(ritprijs(z,False,x))
