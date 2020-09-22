def run():
    mi_diccioanrio = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    # print(mi_diccioanrio['llave2'])
    # print(mi_diccioanrio['llave1'])
    # print(mi_diccioanrio['llave3'])

    poblacion_paises = {
        'argentina': 44000000,
        'brasil': 200000000,
        'chile': 18000000,
    }
    # print(poblacion_paises['argentina'])

    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')

if __name__ == '__main__':
    run()