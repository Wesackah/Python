while True:
    def keuze():
        print('------------------Menu-----------------------')
        print('1: Ik wil weten hoeveel kluizen nog vrij zijn')
        print('2: Ik wil een nieuwe kluis')
        print('3: Ik wil even iets uit mijn kluis halen')
        print('4: Ik geef mijn kluis terug')
        print('-'*48 + '\n')
        gekozen = eval(input(''))
        if gekozen == 1:
            toon_aantal_kluizen_vrij()
        elif gekozen == 2:
            nieuwe_kluis()
        elif gekozen == 3:
            kluis_open()
        elif gekozen == 4:
            kluis_weg()
        else:
            print('je hebt geen geldige waarde opgegeven (1-4)\n')



    def nieuwe_kluis():
        lst_nieuw = []
        lst_alles = [1,2,3,4,5,6,7,8,9,10,11,12]
        infile = open('kluizen.txt', 'r')
        content = infile.readlines()
        for regel in content:
            regel = regel.strip().split(';')
            lst_nieuw.append(regel[0])
            if int(regel[0]) in lst_alles:
                lst_alles.remove(int(regel[0]))
        infile.close()
        if len(lst_nieuw) == 12:
            print('Alle kluizen zijn bezet')
        else:
            print(f'{lst_alles} zijn nog vrij')
            nieuw_nr = input('kies een kluis:  ')
            if nieuw_nr == '':
                print('Je hebt geen geldige waarde gekozen1 (1-12)\n')
            elif int(nieuw_nr) < 1 or int(nieuw_nr) > 12:
                print('Je hebt geen geldige waarde gekozen2 (1-12)\n')
            elif str(nieuw_nr) in lst_nieuw:
                print('deze kluis is al gekozen\n')
            else:
                nieuw_ww = str(input('kies een wachtwoord van minimaal 4 tekens:   '))
                if len(nieuw_ww) < 4:
                    print('Wachtwoord is tekort')
                else:
                    outfile = open('kluizen.txt', 'a+')
                    outfile.write(nieuw_nr + ';' )
                    outfile.write(nieuw_ww + '\n')
                    outfile.close()
                    print(f'U heeft kluis nummer {nieuw_nr} gekozen\n')


    def kluis_open():
        lst_open = []
        lst_ww = []
        infile = open('kluizen.txt', 'r')
        content = infile.readlines()
        for regel in content:
            regel = regel.strip().split(';')
            lst_open.append(regel[0])
            lst_ww.append(regel[1])
        if lst_open == []:
            print('Er zijn nog geen kluizen bezet\n')
        else:
            open_nr = input('Wat is uw kluisnummer?   ')
            if open_nr == '':
                print('Je hebt geen geldige waarde gekozen (1-12)\n')
            elif type(eval(open_nr)) == int:
                if int(open_nr) >= 1 and int(open_nr) <= 12:
                    if open_nr in lst_open:
                        ww = input('Wat is uw wachtwoord?    ')
                        if len(ww) < 4:
                            print('Wachtwoord is te kort (minimaal 4 tekens)\n')
                        else:
                            if ww in lst_ww:
                                if lst_ww.index(ww) == lst_open.index(open_nr):
                                    print('U kunt de kluis openen\n')
                                else:
                                    print('Incorrect wachtwoord\n')
                            else:
                                print('Incorrect wachtwoord\n')
                    else:
                        print('Deze kluis is niet in gebruik\n')
                else:
                    print('Je hebt geen geldige waarde gekozen (1-12)\n')
            else:
                print('Je hebt geen geldige waarde gekozen (1-12)\n')
        infile.close()


    def kluis_weg():
        lst_open_weg = []
        lst_ww_weg = []
        ww_check_weg = []
        open_nr_weg = input('Wat is uw kluisnummer?   ')
        infile = open('kluizen.txt', 'r')
        content = infile.readlines()
        for regel in content:
            regel = regel.strip().split(';')
            lst_open_weg.append(regel[0])
            lst_ww_weg.append(regel[1])
        infile.close()
        if open_nr_weg == '':
            print('Je hebt geen geldige waarde gekozen (1-12)\n')
        elif type(eval(open_nr_weg)) == int:
            if int(open_nr_weg) >= 1 and int(open_nr_weg) <= 12:
                if open_nr_weg in lst_open_weg:
                    ww_weg = input('Wat was uw wachtwoord?   ')
                    if len(ww_weg) < 4:
                        print('Wachtwoord is te kort \n')
                    else:
                        if ww_weg in lst_ww_weg:
                            if lst_ww_weg.index(ww_weg) == lst_open_weg.index(open_nr_weg):
                                outfile = open('kluizen.txt', 'w')
                                outfile.close()
                                for i in range(0,len(lst_ww_weg)):
                                    if i != lst_ww_weg.index(ww_weg):
                                        writefile = open('kluizen.txt', 'a')
                                        writefile.write(lst_open_weg[i] + ';')
                                        writefile.write(lst_ww_weg[i] + '\n')
                                        writefile.close()
                                print('Uw kluisje is vrijgegeven\n')
                            else:
                                print('Incorrect wachtwoord\n')
                        else:
                            print('Incorrect wachtwoord\n')
                else:
                    print('Deze kluis is niet in gebruik\n')
            else:
                print('Je hebt geen geldige waarde gekozen (1-12)\n')
        else:
            print('Je hebt geen geldige waarde gekozen (1-12)\n')


    def toon_aantal_kluizen_vrij():
        lst_bezet = []
        lst_alle = [1,2,3,4,5,6,7,8,9,10,11,12]
        infile = open('kluizen.txt', 'r')
        content = infile.readlines()
        for regel in content:
            regel = regel.strip().split(';')
            lst_bezet.append(regel[0])
            if int(regel[0]) in lst_alle:
                lst_alle.remove(int(regel[0]))
        infile.close()
        print(f'Er zijn {12 - len(lst_bezet)} kluizen vrij')
        print(f'{lst_alle} \n')



    keuze()