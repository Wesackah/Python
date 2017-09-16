def new_password():
    oldpassword = 'jannes2'
    newpassword = input('Voer je nieuwe wachtwoord in')
    if newpassword != oldpassword and len(newpassword) >= 6 :
       if any(str.isdigit(c) for c in newpassword):
           print('Nieuw wachtwoord voldoet')
       else:
           print('er moet een cijfer in het wachtwoord')
    else:
        print('false')

new_password()