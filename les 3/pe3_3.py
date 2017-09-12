leeftijd = eval(input('Wat is je leeftijd? '))
paspoort = input('Heb je een paspoort? ja/nee?')
if leeftijd >= 18 and paspoort == 'ja':
    print('Gefeliciteerd, je mag stemmen!')

else:
    print('Je mag niet stemmen!')