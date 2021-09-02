# Heredar de la clase Auto una clase Marca, 
# que agregue el atributo Modelo. 
# Instanciar en  el programa principal 
# (una sola línea en total).
# La salida debe ser por ejemplo:
# Auto: VW Modelo: Gol

class Car():
    def __init__(self,march,year):
        self.march = march
        self.year = year
    def antiquity(self):
        return 2021-self.year
class March(Car):
    def __init__(self,mch,yr,model):
        super().__init__(mch,yr)
        self.model = model
        print('Car:',self.march,'Model:',self.model)
if __name__ == '__main__':
    March('VW',2018,'Gol')