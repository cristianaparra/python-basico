def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input('Escribe una palabra: ')
    es_palindormo = palindromo(palabra)
    if es_palindormo == True:
        print('es palindormo')
    else:
        print('no es palindromo')


if __name__ == '__main__':
    run()

