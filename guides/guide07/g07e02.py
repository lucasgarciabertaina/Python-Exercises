# Definir una clase Auto con un método que le 
# permita poner la marca y el año. En el programa
# principal declarar tres instancias (objetos),
# cargarlas y mostrar las marcas de los tres 
# autos
class Car():
    def __init__(self,march,year):
        self.march = march
        self.year = year
    def getMarch(self):
        return self.march

if __name__ == '__main__':
    car1 = Car('Audi',2018)
    car2 = Car('Renaut',2015)
    car3 = Car('Bmw',2021)
    print(car1.getMarch(),car2.getMarch(),car3.getMarch())

