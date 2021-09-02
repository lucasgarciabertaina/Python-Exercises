#6) Crear una aplicación para gestionar un videoclub.
#Todos los productos tienen:
#Titulo, precio alquiler, plazo(dias), alquilado (si/no)
#Genero (accion, fantasía, etc), año, director, protagonista
#Se mantiene un listado de clientes:
#– Nº cliente, nombre, dirección, teléfono, productos alquilados
#Se guarda un listado de registros de alquiler:
#– Cliente, producto, fecha alquiler, fecha devolucion, importe
#Crear una aplicación de consola con el siguiente menú:
#– Lista productos
#– Añadir producto
#– Ficha producto
#– Lista clientes
#– Añadir cliente
#– Ficha cliente
#– Alquiler producto

class Film():
    def __init__(self,title,genere,year,director,protagonist):
        self.filmTitle = title
        self.filmGenere = genere
        self.filmYear = year
        self.filmDirector = director
        self.filmProtagonist = protagonist
    def getFilm(self):
        return {'Title':self.filmTitle,'Genere':self.filmGenere,'Year': self.filmYear,'Director':self.filmDirector,'Protagonist':self.filmProtagonist}
    def getTitle(self):
        return self.filmTitle

class Product(Film):
    def __init__(self,title,genere,year,director,protagonist,price,deadline,rented):
        self.producTitle = title
        self.productPrice = price
        self.productDeadLine = deadline
        self.productRented = rented
        Film.__init__(self,title,genere,year,director,protagonist)
    def rent(self):
        self.productRented = True

class Client():
    def __init__(self,name,product,dayRented,dayReturn,price):
        self.clientName = name
        self.clientProduct = product
        self.clientDayRented = dayRented
        self.clientDayReturn = dayReturn
        self.clientPrice = price
    def getClient(self):
        return {'Name':self.clientName,'Product':self.clientProduct,'Day Rented': self.clientDayRented,'Day Return':self.clientDayReturn,'Price':self.clientPrice}
    def getName(self):
        return self.clientName


products = [
    Product('Harry Potter','Drama',2008,'Pablito Kan','Yo (obvio)',70,7,False),
    Product('Cars','Comedy',2006,'Palma','Pablo el rey de reyes',5,9,False),
    Product('Stuart Little','Fantasy',2000,'El director','Palma',8,2,False)
]

clients = [
    Client('Lucas',products[0].producTitle,'01/09/2021','08/09/2021',products[0].productPrice),
    Client('Pablo',products[1].producTitle,'01/09/2021','10/09/2021',products[1].productPrice)
]

def getProducts(elemnts):
    for e in elemnts:
        print(e.getTitle())

def setProduct(elements):
    elements.append(Product(input('Film name: '),input('Film genere: '),int(input('Film year: ')),input('Film director: '),input('Film protagonist: '),int(input('Film price:' )),input('Film deadline: '),True if input('Its rented? ') == 'y' else False))

def getFilm(product):
    for key,value in product.getFilm().items():
        print(key,value)

def getClients(elements):
    for e in elements:
        print(e.getName())

def setClient(elements):
    elements.append(Client(
        input('Name: '),
        input('Product:' ),
        input('Day rented: '),
        input('Day return: '),
        int(input('Price: '))
    ))

def getClient(client):
    for key,value in client.getClient().items():
        print(key,value)

def options():
    print('- List of products (1)')
    print('– Add product (2)')
    print('– Product sheet (3)')
    print('– Customer list (4)')
    print('– Add customer (5)')
    print('– Customer file (6)')
    print('– Product rental (7)')
    print('- Exit (8)')
def main():
    options()
    option = int(input())
    while option != 8:
        if option == 1:
            print(getProducts())
            options()
        elif option == 2:
            setProduct(products)
            options()
        elif option == 3:
            for product in products:
                print(product.getTitle(),'(',products.index(product),')')
            productChoise = int(input())
            getFilm(products[productChoise])
            options()
        elif option == 4:
            print(getClients())
            options()
        elif option == 5:
            setClient(clients)
            options()
        elif option == 6:
            for client in clients:
                print(client.getName(),'(',clients.index(client),')')
            clientChoise = int(input())
            getClient(clients[clientChoise])
            options()
        elif option == 7:
            for product in products:
                print(product.getTitle(),'(',products.index(product),')')
            productChoise = int(input())
            products[productChoise].rent()
            options()

if __name__ == '__main__':
    main()
