#3) Crea las siguientes clases (cada una en su archivo): 
# Motor: con métodos para arrancar el motor y apagarlo. 
# Rueda: con métodos para inflar la rueda y desinflarla. 
# Ventana: con métodos para abrirla y cerrarla. 
# Puerta: con una ventana y métodos para abrir la puerta y cerrar la puerta. 
# Coche: con un motor, cuatro ruedas y dos puertas;  con los métodos que te parezcan

class Engine():
    def __init__(self):
        self.engineState = False
    def startUp(self):
        self.engineState = True
    def shutDown(self):
        self.engineState = False
    def getEngineState(self):
        if self.engineState:
            print('Engine is on')
        else:
            print('Engine is off')
class Wheels():
    def __init__(self):
        self.wheelState = False
    def inflate(self):
        self.wheelState = True
    def deflate(self):
        self.wheelState = False
    def getWheelsState(self):
        if self.wheelState:
            print('Wheels are inflate')
        else:
            print('Wheels are deflate')
class Windows():
    def __init__(self):
        self.windowState = False
    def openWIndow(self):
        self.windowState = True
    def closeWindow(self):
        self.windowState = False
    def getWindowState(self):
        if self.windowState:
            print('Windows are open')
        else:
            print('Windows are close')
class Doors():
    def __init__(self):
        self.doorsState = False
    def openDoors(self):
        self.doorsState = True
    def closeDoors(self):
        self.doorsState = False
    def getDoorsState(self):
        if self.doorsState:
            print('Doors are open')
        else:
            print('Doors are close')
class Car(Engine,Wheels,Windows,Doors):
    def __init__(self):
        Engine.__init__(self)
        Wheels.__init__(self)
        Windows.__init__(self)
        Doors.__init__(self)
        self.conditions = False
    def setConditions(self):
        Engine.startUp(self)
        Wheels.inflate(self)
        Windows.openWIndow(self)
        Doors.openDoors(self)
    def getConditions(self):
        print('===CAR STATE===')
        Engine.getEngineState(self)
        Wheels.getWheelsState(self)
        Windows.getWindowState(self)
        Doors.getDoorsState(self)
        if self.engineState and self.wheelState and self.windowState and self.doorsState:
            print('The car is OK')
        else:
            print('The conditions isnt Ok')
        print('==============')
if __name__ == '__main__':
    car1 = Car()
    car1.deflate()
    car1.getDoorsState()
    car1.setConditions()
    car1.getWheelsState()
    car1.getConditions()