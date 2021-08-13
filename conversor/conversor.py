menu = """
Bienvenido al conversor de monedas 

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción:
"""

opcion = input(menu)

if opcion == "1":

    pesos = input("¿Cuantos pesos colombianos tienes? ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
    
elif opcion == "2":

    pesos = input("¿Cuantos pesos argentinos tienes? ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

elif opcion == "3":

    pesos = input("¿Cuantos pesos mexicanos tienes? ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

else:
    print("Imprime una opción correcta por favor")
