#Agregar al ejercicio 2 (clase Auto) un método 
#que obtenga la antigüedad. En el programa
#principal mostrar cuáles autos tienen más de
#5 años.
class Car():
    def __init__(self,march,year):
        self.march = march
        self.year = year
    def getMarch(self):
        return self.march
    def antiquity(self):
        return 2021-self.year
    
def more5(years):
    if years > 5:
        return True
    return False

if __name__ == '__main__':
    cars = []
    cars.append(Car('Audi',2018))
    cars.append(Car('Renaut',2015))
    cars.append(Car('Bmw',2021))
    for car in cars:
        if more5(car.antiquity()):
            print(car.march)
