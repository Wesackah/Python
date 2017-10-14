invoer = input('aantal personen:  ')
try:
    if int(invoer) < 0:
        print('negatief kan niet')
    else:
        x = 4356/int(invoer)
        print(x)
except ValueError:
    print('een getal aub')
except ZeroDivisionError:
    print('kan niet delen door 0')

