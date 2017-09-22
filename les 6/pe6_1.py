def seizoen(maand):
    lente = [3, 4, 5]
    zomer = [6, 7, 8]
    herfst = [9, 10, 11]
    winter = [12, 1, 2]

    if maand in lente:
        print('lente')
    else:
        if maand in zomer:
            print('zomer')
        else:
            if maand in herfst:
                print('herfst')
            else:
                if maand in winter:
                    print('winter')
                else:
                    print('Je hebt een verkeerde waarde gegeven')

seizoen(eval(input('geef het maandnummer')))
