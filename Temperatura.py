def promedio_temperatura(temperaturas):
    sum_of_temps=0
    for temp in temperaturas:
        sum_of_temps += temp
    return sum_of_temps / len(temperaturas)

if __name__ == '__main__':

    temperaturas=[21,24,24,22,20,23,24]

    promedio=promedio_temperatura(temperaturas)

    print('')
    print(' La temperatura promedio es: {}'.format(promedio))