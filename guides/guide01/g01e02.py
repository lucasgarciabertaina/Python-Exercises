
""" Pedir tres notas, calcular el promedio y mostrarlo.
 """

note1 = int(input('Ingrese la primera nota: '))
note2 = int(input('Ingrese la segunda nota: '))
note3 = int(input('Ingrese la tercera nota: '))

add = note1+note2+note3
prom = add/3

print('El promedio entre nota 1: ',note1,', nota 2: ',note2,', nota3: ',note3,' es:',prom)