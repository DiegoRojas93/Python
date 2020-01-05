Number=int(input('Ingresa un numero: '))

for i in range(Number):
    if i%3 != 0:
        continue # continua la iteraciion
    else:
        print(i)

Number=int(input('Ingresa otro numero: '))

for i in range(Number):
    if i%3 == 0:
        print(i)
    elif i==22:
        break # sale de la iteracion
