def is_prime(number):
  if number < 2:
    return False
  elif number ==2:
    return True
  elif number > 2 and number%2 == 0:
    return False
  else:
    for i in range (3, number): #probar todos los numero des de 3 hasta el numero que ponesen consola
      if number%i ==0: # Si el numero es divisible con el rango que generamos
        return False
  return True


def run():
  number=int(input('Escribe un nuemro: '))
  result=is_prime(number)

  if result is True:
    print('Tu numero es primo')
  else:
    print('Tu numero No es primo')


if __name__ == '__main__':
  run()