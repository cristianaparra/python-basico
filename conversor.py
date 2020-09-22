def conversor(tipos_pesos, valor_dolar): 
    pesos = input('¿cuantos pesos '+ tipos_pesos +' tienes?: ')
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('tienes $' + dolares + ' dolares')

menu = '''
Bienvenidos al convewrsor de monedas🇦🇲

1 - pesos chilenos
2 - pesos argentinos
3 - pesos mexicanos

elige una opcion: 
'''

opcion = int(input(menu))

if opcion == 1:
    conversor('chilenos', 750)
    
elif opcion == 2:
   conversor('argentinos', 150)
    
elif opcion == 3:
    conversor('mexicanos', 24)
    
else:
   print('ingresa una opcion valida')

