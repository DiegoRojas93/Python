def binary_search(numbers, number_to_find, low, high):
  
  if low > high: # caso base si no encontramos el numero
    return False
  
  mid = int((low + high) / 2)

  if numbers[mid] == number_to_find: # caso base SI encontramos el numero por mucha casualidad
    return True
  elif numbers[mid] > number_to_find:  # caso base si el numero de la lista es más grande al numero a encontar
    return binary_search(numbers, number_to_find, low, mid-1)
  else: # caso base si el numero de la lista es menor al numero a encontar
    return binary_search(numbers, number_to_find, mid+1, high)


if __name__ == '__main__':
  numbers=[1, 3, 4, 5, 6, 9, 10, 11, 25,27, 28, 34, 36, 49, 51]
  
  number_to_find = int(input(' Ingresa un numero: ')) # Buscar numero

  result = binary_search(numbers, number_to_find, 0, len(numbers)-1)

  if result is True:
    print(' El numero sí esta en la lista.')
  else:
    print(' El numero NO esta en la lista.')