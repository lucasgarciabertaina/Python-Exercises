# Hacer una clase Teléfono con los atributos marca
# ,modelo y costo mensual y un método que muestre (o devuelva) el costo anual.

class Phones():
    def __init__(self,model,march,monthCost):
        self.model = model
        self.march = march
        self.monthCost = monthCost
    def getData(self):
        return self.model, self.march, self.monthCost

if __name__ == '__main__':
    phone1 = Phones('A20','Samsung',300)
    modl,mch,cost = phone1.getData()
    print(modl,mch,cost)