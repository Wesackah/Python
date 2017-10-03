x = eval(input('geef cijfer'))
lst = []
count = 0
while x != 0:
    x = eval(input('geef cijfer2'))
    lst.append(x)
    count = count + 1
if x == 0:
    print(f'lengte is {count}')
    print(f'som is {sum(lst)}')
