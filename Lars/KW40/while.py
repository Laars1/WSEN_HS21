x = 0

while x < 10:
    print('x ist aktuell: ',x)
    print(' x ist immer noch kleiner als 10, 1 zu x hinzufügen')
    x += 1
    if x == 3:
        print('x == 3')
    else:
        print('Fortsetzen...')
        continue