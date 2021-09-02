# Hacer una clase Persona con dos métodos:
# uno para saber si es mayor de edad y el otro
# para determinar si es varón o mujer.
# En el programa principal instanciarlo, 
# tomar nombre, edad y sexo, y finalmente
# mostrar un cartel que diga por ejemplo 
# ‘Juan es mayor de edad y es varón’.
class Person():
    def legalAge(self,age):
        self.age = age
        if self.age >= 18:
            self.legal = 'mayor'
        else:
            self.legal = 'menor'
    def genere(self,name,sex):
        self.name = name
        self.sex = sex
        if self.sex == 'mujer':
            print(self.name,'es',self.legal,'y es mujer')
        else:
            print(self.name,'es',self.legal,'y es varon')

if __name__ == '__main__': 
    person1 = Person()
    person1.legalAge(16)
    person1.genere('Juan','varon')
