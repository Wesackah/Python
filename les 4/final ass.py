def standaardprijs(afstandKM):
     if afstandKM > 50:
        kost = 15 + (afstandKM - 50)*.6
        return kost
     else:
        if afstandKM <= 0:
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

x = 20
print(standaardprijs(x))
print(ritprijs(15,True,x))
