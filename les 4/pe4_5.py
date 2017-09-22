def kwadraten_som(grondgetallen):
    totaal = 0
    for i in grondgetallen:
        if i > 0:
            totaal += i**2
    return totaal
print(kwadraten_som( [ 4, 5, 3, -81 ]))


def kw_som(lst):
    kwSom = 0
    for getal in lst:
        kwSom = kwSom + getal**2
    return kwSom

print(kw_som([4,5,3]))
