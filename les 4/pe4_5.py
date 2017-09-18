def kwadraten_som(grondgetallen):
    totaal = 0
    for i in grondgetallen:
        if i > 0:
            totaal += i**2
    return totaal
print(kwadraten_som( [ 4, 5, 3, -81 ]))

