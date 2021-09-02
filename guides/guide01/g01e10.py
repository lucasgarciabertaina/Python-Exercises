""" 
Preguntar nombre, carrera en la que se 
inscribe y ciudad donde vive un ingresante
al Instituto. Los estudiantes de la carrera
de Electromecánica y que no viven en
Río Cuarto tendrán un 15% de descuento
en la cuota que es de $4500. Mostrar nombre, 
ciudad, carrera y monto final de la cuota.
 """
name = input('¿Cúal es su nombre? ')
career = input('Carrera a inscribirse: ')
city = input('Ciudad de residencia: ')
payment = 4500
if career == 'Electromecánica' and city != 'Río Cuarto':
    discount = 45*15
    print(name, '-', city, '-', career, '-$', payment-discount)
else:
    print(name, '-', city, '-', career, '-$', payment)
