hora = input('Que horas são? ')

if hora.isdigit():
    hora = int(hora)
    if hora >= 0 and hora <=11:
        print('Good Morning!')
    elif hora>= 12 and hora <=17:
        print('Good Afternoom')
    elif hora>= 18 and hora <=23:
        print('Good Evening')
    else:
        print('Hora invalida!')
else:
    print('Hora invalida!')