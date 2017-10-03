def namen():
    dic = {}
    while True:
        vraag = input('naam?')
        if vraag == '':
            break
        else:
            if vraag in dic:
                dic[vraag] += 1
            else:
                dic.update({vraag:1})

    for naam,maal in dic.items():
        if maal <=1:
            print('er is {} met naam {}'.format(naam,maal))
        else:
            print('er zijn {} met naam {}'.format(naam, maal))

namen()