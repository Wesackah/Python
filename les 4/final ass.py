def standaardprijs(afstandKM):
     if afstandKM > 50:
        if afstandKM >= 0:
            kost = 0
            return kost
        else:
            kost = 15 + afstandKM*0.6
            return kost
     else:
        kost = afstandKM*0.8
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


print(ritprijs(68, False, 50))
