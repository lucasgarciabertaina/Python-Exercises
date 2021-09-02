#2) Desarrolla una clase Cafetera con atributos capacidadMaxima (la cantidad máxima de café que puede contener
# la cafetera) y cantidadActual (la cantidad actual de café que hay en la cafetera). Implementa, al menos,
# los siguientes métodos: 
#Constructor: establece la capacidad máxima en 1000 (c.c.)  y la actual en cero (cafetera vacía). 
#llenarCafetera(), servirTaza(int): simula la acción de servir una taza con la capacidad indicada, si la
# cantidad actual de café no alcanza para llenar la taza, se sirve lo que quede. 
#vaciarCafetera(): pone la cantidad de café actual en cero.  
#mostrarCafetera(): nos dice cuanto café hay.


class CoffeMachine():
    def __init__(self):
        self.maximunCapacity = 1000
        self.actualCapacity = 0
    def fillCoffeMachine(self):
        self.actualCapacity = self.maximunCapacity
    def servingCoffe(self,quantity):
        self.quantity = quantity
        if self.quantity < self.actualCapacity:
            self.actualCapacity -= self.quantity
        else:
            self.actualCapacity = 0
    def emptyCoffeMachine(self):
        self.actualCapacity = 0
    def getCoffeMachine(self):
        print('There are/is',self.actualCapacity,'(c.c)')

if __name__ == '__main__':
    myCoffeMachine = CoffeMachine()
    myCoffeMachine.fillCoffeMachine()
    myCoffeMachine.servingCoffe(350)
    myCoffeMachine.getCoffeMachine()
