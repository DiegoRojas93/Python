# -*- coding: utf-8 -*-

KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}

def cifrar(mensaje):
    palabras=mensaje.split(' ') # Crea una lista de las palbras del mensaje
    cifrar_mensaje = [] # Crea una lista vacia llamada cifrar mensaje

    for palabra in palabras: # Para cada palabra de las palabras
        cifrar_palabra = '' # declaramos una variable vacia
        for letra in palabra: # para cada letra de la palabra
            cifrar_palabra += KEYS[letra] 
            # cada letra sirve como llave y lo regresa como su valor
            # a la variable cifrar_palabra

        cifrar_mensaje.append(cifrar_palabra)
        # por cada iteracion terminada, la palabra queda guardada en
        # la lista vacia llamada cifrar mensaje
    
    return ' '.join(cifrar_mensaje) #se reconstruye el mensaje
    # por casa espacio ponga la palabla cifrada


def decifrar(mensaje):
    palabras = mensaje.split(' ') # Crea una lista de las palbras del mensaje cifrado
    decifrar_mensaje = [] # Crea una lista vacia llamada decifrar mensaje

    for palabra in palabras: # Para cada palabra de las palabras
        decifrar_palabra = '' # declaramos una variable vacia

        for letra in palabra:  # para cada letra de la palabra
            for key, value in KEYS.items():
                # Por cada llave y cada valor del item
                if value == letra:
                    decifrar_palabra += key #Guarda la llave
                    # en la vaiable decifrar_palabra
      
        decifrar_mensaje.append(decifrar_palabra)
        # por cada iteracion terminada, la palabra queda guardada en
        # la lista vacia llamada decifrar mensaje
    
    return ' '.join(decifrar_mensaje) #se reconstruye el mensaje
    # por casa espacio ponga la palabla decifrada



def run():

    while True:

        command = str(input('''--- * --- * --- * --- * --- * --- * --- * ---

            Bienvenido a criptografía. ¿Qué deseas hacer?

            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
        '''))

        if command == 'c':
            mensaje=str(input(' Escribe tu mensaje: '))
            cifrar_mensaje = cifrar(mensaje)
            print(' {}'.format(cifrar_mensaje))
        elif command == 'd':
            mensaje=str(input(' Escribe tu mensaje cifrado: '))
            decifrar_mensaje = decifrar(mensaje)
            print(' {}'.format(decifrar_mensaje))
        elif command == 's':
            print('salir')
        else:
            print('¡Comando no encontrado!')


if __name__ == '__main__':
    print('M E N S A J E S  C I F R A D O S')
    run()