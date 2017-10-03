import random

def Monopolyworp():
    count = 0
    while True:
        x = random.randrange(1,7)
        y = random.randrange(1,7)
        z = x + y
        if x != y:
            print(f'{x}+{y} = {z}')
            break
        else:
            count = count + 1
            print(f'{x}+{y} = {z}')
            if count == 3:
                print(f'{x}+{y} = {z}')
                print('gevangenis')
                break


Monopolyworp()