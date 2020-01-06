import time

def factorial(temporizador):
    print('')
    print(temporizador)
    time.sleep(1)
    if temporizador==0:
        print ('Boooooooom!')
        return 1
    return temporizador * factorial(temporizador-1)

def Desafio(Number,palabra):
    if Number==1:
        palabra_inversa=palabra[::-1]
        if palabra_inversa==palabra:
            return True
        return False

    elif Number==2:
        letras_inversas=[]

        for letra in palabra:
            letras_inversas.insert(0, letra)
    
        palabra_inversa=''.join(letras_inversas)

        if palabra_inversa==palabra:
            return True

        return False

    else:
        temporizador=int(input(' Ingresa el tiempo en segundos: '))
        
        factorial(temporizador)

  

if __name__ == '__main__':

    print('')
    Number=int(input( ' Elige el desafio, del 1 al 3: '))
    print('')
    palabra=str(input(' Escribe una palabra: '))

    result=Desafio(Number,palabra)

    if result is True:
        print('')
        print(' {} si es un palíntromo'.format(palabra))
        
    else:
        print('')
        print(' {} no es un palíntromo'.format(palabra))
