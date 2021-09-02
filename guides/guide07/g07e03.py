# Usando las clases Operacion y Suma, definir
# otra que se llame Promedio y utilizarla
class Operation():
    def __init__(self):
        self.elements = []
        confirmation = input('Whould you like to input any data? (Y/n)')
        while confirmation != 'n':
            self.elements.append(input('Insert\n'))
            confirmation = input('Whould you like to input any data? (Y/n)')
    def simpleOperates(self):
        self.result = None
    def complexOperates(self):
        self.result = None
    def getResult(self):
        return self.result

class Sum(Operation):
    def simpleOperates(self):
        self.total = 0
        for e in self.elements:
            self.total += int(e) 
        self.values = len(self.elements)
        self.result = self.total

class Average(Sum):
    def complexOperates(self):
        self.result = self.result/len(self.elements)

if __name__ == '__main__':
    average = Average()
    average.simpleOperates()
    average.complexOperates()
    print(average.getResult())