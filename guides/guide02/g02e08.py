"""
Ingresar autos y sus precios y contar cuantos
valen entre $1.460.000 y $2.850.000. Terminar
la carga cuando el valor ingresado sea $0.
"""
price = 1
condition = 0
while price != 0:
    car = input('Car brand: ')
    price = int(input('Price: '))
    if price >= 1460000 and price <= 2850000:
        condition = condition + 1

print('1460000 >= price <= 2850000 are ', condition)
