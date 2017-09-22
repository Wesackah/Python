def gemiddelde():
    tekst = input('schrijf iets?')
    tekst = tekst.strip().split(' ')
    lengte = 0
    count = 0
    for i in tekst:
        lengte +=len(i)
        count = count + 1
    print(lengte/count)

gemiddelde()
