def run(Ejercicio):
    if Ejercicio==1:
        print('')
        titulo=('DIVISOR DE NUMEROS')
        T=titulo.center(87,'*')
        print(T)
        print('')

        n1=int(input(' Escribe el Dividendo: '))
        n2=int(input(' Escribe el divisor: '))

        if n1 % n2 == 0:
            print(' La divicion es exacta')
        else:
            cociente=float(n1/n2)
            resto=int(n1/n2)
            print(' La divicion no es exacta. Su conciente es {} y el resto es {}'.format (cociente, resto))

    if Ejercicio==2:
        print('')
        titulo=('DIVISION POR CERO')
        T=titulo.center(87,'*')
        print(T)
        print('')

        n1=int(input(' Escribe el Dividendo: '))
        n2=int(input(' Escribe el divisor: '))

        if n2 == 0:
            print(' No se puede dividir por cero')

        elif n1 % n2 == 0:
            print(' La divicion es exacta')
        else:
            cociente=float(n1/n2)
            resto=int(n1/n2)
            print(' La divicion no es exacta. Su conciente es {} y el resto es {}'.format (cociente, resto))

    if Ejercicio==3:
        print('')
        titulo=('COMPARADOR DE NUMEROS')
        T=titulo.center(87,'*')
        print(T)
        print('')

        n1=int(input(' Escribe un número: '))
        n2=int(input(' Escribe otro núemro: '))

        if n1==n2:
            print(' El número {} y el número {} son iguales'.format(n1,n2))
        elif n1>n2:
            print(' El número {} es mayor que el número {}'.format(n1,n2))
        else:
            print(' El número {} es menor que el número {}'.format(n1,n2))

    if Ejercicio==4:

        print('')
        titulo=('COMPARADOR DE AÑOS')
        T=titulo.center(87,'*')
        print(T)
        print('')

        age1=int(input(' ¿En qué año estamos?: '))
        age2=int(input(' Escriba un año cualquiera (pueder ser del pasado ó del futuro): '))

        if age1==age2:
            print(' {} y {} ¡Son el mismo año!'.format(age1,age2))
        elif age1<age2:
            age_remaining=age2-age1
            print(' Para llegar al año {} faltan {} años'.format(age2, age_remaining))
        else:
            age_elapsed=age1-age2
            print(' Desde el año{} han pasado {} años'.format(age2, age_elapsed))

    if Ejercicio==5:

        print('')
        titulo=(' COMPARADOR DE MULTIPLOS')
        T=titulo.center(87,'*')
        print(T)
        print('')

        n1=int(input(' Escribe un número: '))
        n2=int(input(' Escribe otro núemro: '))

        if (n1%n2)==0 or (n2%n1)==0:
            if n1>n2:
                print(' {} es múltiplo de {}' .format(n1,n2))
            else:
                print(' {} es múltiplo de {}' .format(n2,n1))
        else:
            print(' {} no es múltiplo de {}' .format(n2,n1))

    if Ejercicio==6:
        print('')
        titulo=('COMPARADOR DE 3 TRES NÚMEROS')
        T=titulo.center(87,'*')
        print(T)
        print('')

        n1=int(input(' Escribe un número: '))
        n2=int(input(' Escribe otro núemro: '))
        n3=int(input(' Escribe otro número más: '))

        if (n1==n2!=n3) or (n1==n3!=n2) or (n3==n2!=n1):
            print(' Ha escrito 2 veces el mismo número.')
        elif n1==n2==n3:
            print(" Ha escrito tres veces el mismo número.")
        else:
            print(" Los tres números que ha escrito son distintos.")

    if Ejercicio==7:

        print('')
        titulo=('COMPARADOR DE AÑOS BICIESTOS')
        T=titulo.center(87,'*')
        print(T)
        print('')

        print(' El año biciesto es aquel año que tiene un día más')
        print('')
        age=int(input(' Escriba un año y le diré si es bisiesto: '))

        if (age%400==0):
            print('')
            print(' El año {} es un año bisiesto porque es múltiplo de 400.'.format(age))
        elif (age%100==0):
            print('')
            print(' El año {} no es un año bisiesto porque es múltiplo de 100 sin ser múltiplo de 400.'.format(age))
        elif (age%4==0):
            print('')
            print(' El año {} es un año bisiesto porque es múltiplo de 4 sin ser múltiplo de 100.'.format(age))
        else:
            print('')
            print(' El año {} no es un año bisiesto'.format(age))

    if Ejercicio==8:
        print('')
        titulo=('ECUACION aX + B =0')
        T=titulo.center(87,'*')
        print(T)
        print('')

        a=float(input('Escriba el valor del coeficiente a: '))
        b=float(input('Escriba el valor del coeficiente b: '))

        if a==0 and (b!=0):
            print('')
            print('La ecuación no tiene solución.')

        elif a==0 and b==0:
            print('')
            print('Todos los números son solución.')
        else:
            x=-b/a
            print('')
            print('La ecuación tiene una solución: {}'.format(x))

    if Ejercicio==9:
        print('')
        titulo=('ECUACION ax**2 +bX +C = 0')
        T=titulo.center(87,'*')
        print(T)
        print('')

        a=float(input('Escriba el valor del coeficiente a: '))
        b=float(input('Escriba el valor del coeficiente b: '))
        c=float(input('Escriba el valor del coeficiente c: '))

        d = b * b - 4 * a * c
        if a==b==c==0:
            print('Todos los números son solución')
        elif a==b==0:
            print('La ecuación no tiene solución')
        elif a==0:
            x=-c / b
            print('La ecuación tiene una solución: {}'.format(x))
        elif d < 0:
            print('La ecuación no tiene solución real.')
        elif d == 0:
            x=-b / (2 * a)
            print('La ecuación tiene una solución: {}'.format(x))
        else:
            x1=(-b - d ** 0.5) / (2 * a)
            x2=(-b + d ** 0.5) / (2 * a)
            print('La ecuación tiene dos soluciones: {} y {}'. format(x1 ,x2))

if __name__ =='__main__':
    print('')
    Ejercicio=int(input(' Elige un ejercicio del uno al siete: '))
    run(Ejercicio)
