# Redefinir la clase auto con los atributos marca
# , modelo y año. Hacer una clase heredera
# TuAuto que agrega dueño y color. Hacer un
# método que devuelve el color y en el programa
# principal preguntar por un color y
# mostrar sólo los autos que cumplan esa
# condición.

class Car():
    def __init__(self,march,model,year):
        self.march = march
        self.model = model
        self.year = year
    def antiquity(self):
        return 2021-self.year
class yourCar(Car):
    def __init__(self,mch,mdl,yr,owner,color):
        super().__init__(mch,mdl,yr)
        self.owner = owner
        self.color = color
    def getColor(self):
        return self.color
    def showCar(self):
        print('Car:',self.march,'Model:',self.model,'Color:',self.color,'Owner:',self.owner)
if __name__ == '__main__':
    cars = [yourCar('VW','Gol Trend',2018,'Lucas','blue'),yourCar('BMW','M3',2015,'Colo','red'),yourCar('Renaut',12,2004,'El profe','blue'),yourCar('Peugeot',305,2007,'Damian','green')]
    color = input('What color would you like the car to be?\n')
    for car in cars:
        if color == car.getColor():
            car.showCar()


