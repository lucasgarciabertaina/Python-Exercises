# Definir una clase Persona cuyo constructor 
# reciba nombre y edad. El programa principal 
# pedirá en forma repetitiva 
# (hasta que no haya más) los mismos datos,
# hará la instanciación de un objeto y lo
# agregará en una lista. 
# Por lo tanto, los elementos de dicha lista
# serán objetos y podrá mostrarse por recorrido
# y/o por subindicación.
class Person():
    def __init__(self):
        self.name = input("What's your name?\n")
        self.age = int(input("How old are you?\n"))

if __name__ == '__main__':
    people = []
    confirmation = input('Whould you like to add a person? (Y/n)')
    while confirmation != 'n':
        people.append(Person())
        confirmation = input('Whould you like to add a person? (Y/n)')
    print(people[0].name)