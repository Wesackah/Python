def convert(cel):
    temp = cel*1.8+32
    return temp


def table():
    for x in range(-30,41,10):
        print('{0:8},{1:8}'.format(convert(x), x))


print('{0:8},{1:8}'.format('      F', '       C'))
table()