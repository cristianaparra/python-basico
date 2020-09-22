import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('elige un numero de 1 a 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('busca mas arriba')
        else:
            print('busca mas abajo')
        numero_elegido = int(input('elige otro numeor perra: '))
    print('!ganaste wachin')


if __name__ == '__main__':
    run()