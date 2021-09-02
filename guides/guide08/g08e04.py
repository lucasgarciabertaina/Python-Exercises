#4) Desarrolla una clase Cancion con los siguientes atributos: titulo y autor
#y los siguientes métodos: 
#constructor que recibe como parámetros el título y el autor de la canción (por este orden). 
#dameTitulo(): devuelve el título de la canción. 
#dameAutor(): devuelve el autor de la canción. 
# ponerTitulo(String):  establece el título de la canción. 
# ponerAutor(String): establece el autor de la canción.
class Song():
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def getTitle(self):
        return self.title
    def getAuthor(self):
        return self.author
    def setTitle(self,newTitle):
        self.title = newTitle
    def setAuthor(self,newAuthor):
        self.author = newAuthor
if __name__ == '__main__':
    mySong = Song('El amanecer','Lucas Garcìa')
    print(mySong.getAuthor())
    print(mySong.getTitle())
    mySong.setAuthor('Pablito')
    print(mySong.getAuthor())
         
