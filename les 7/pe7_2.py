x = input('geef string met 4 tekens')
while len(x) != 4:
    print(f'je gaf een woord met lengte {len(x)}')
    x = input('geef string met 4 tekens')
else:
    print('je woord voldoet')
