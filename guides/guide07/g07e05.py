# Definir una clase que al ser instanciada 
# reciba un valor numérico y cargue una lista
# de nombres hasta esa cantidad. Hacer también
# un método que muestre la lista completa
import random

class Name():
    def __init__(self):
        randomNumber = random.randint(1,10)
        self.elements = []
        for i in range(randomNumber):
            self.elements.append(input('Insert\n'))
    def getNames(self):
        return self.elements

if __name__ == '__main__':
    names = Name()
    print(names.getNames())
