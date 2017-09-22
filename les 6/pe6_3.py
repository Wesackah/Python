def uitvoer():
    invoer ='5-9-7-1-7-8-3-2-4-8-7-9'
    invoer = invoer.strip().split('-')
    lst = []
    for i in invoer:
        lst.append(int(i))
    lst.sort()
    print(f' sorted: {lst}')
    print(f' max: {max(lst)} min: {min(lst)}')
    print(f'lengte:{len(lst)}   som:{sum(lst)}')
    print(f'{sum(lst)/len(lst)}')


uitvoer()