# Definir una clase Telefono, sus atributos son:
# marca, modelo, sistema operativo, plan(costo)
# y cantidad de RAM. 
# Sus métodos son: costo anual, mostrar Sistema
# Operativo y si es gama alta o no
# (con 6 o más gigas de RAM) .
class Phone():
    def __init__(self,march,model,os,cost,ram):
        self.march = march
        self.model = model
        self.os = os
        self.cost = cost
        self.ram = ram
    def anualCost(self):
        return self.cost*12
    def showOS(self):
        return self.os
    def highEnd(self):
        if ram > 6:
            return True
        return False

