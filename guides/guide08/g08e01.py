#1) Crea una clase Cuenta (bancaria) con atributos para el número de cuenta, el DNI del cliente, el saldo actual
#  y el interés anual que se aplica a la cuenta (porcentaje). Define en la clase los siguientes métodos: 
# constructor con DNI, saldo e interés. 
# Método actualizarSaldo(): actualizará el saldo de la cuenta aplicándole el interés diario (interés anual
#  dividido entre 365 aplicado al saldo actual), método ingresar(float):  permitirá ingresar una cantidad en
#  la cuenta, método retirar(float): permitirá sacar una cantidad de la cuenta (si hay saldo).
#  Finalmente, un método que nos permita mostrar todos los datos de la cuenta.
class Account():
    def __init__(self):
        self.dni = int(input('Please insert your D.N.I:\n'))
        self.balance = 0
        self.annualInterest = float(input('Please insert your annual interest:\n'))
        self.accountNumber = input('Please insert your account number:\n')
    def updateBalance(self):
        self.balance += (self.annualInterest/365)
    def inputMoney(self,money):
        self.balance += float(money)
        print(self.balance)
    def removeMoney(self,money):
        self.money = float(money)
        if self.money > self.balance:
            print('Insufficient balance!')
        else:
            self.balance -= self.money
    def getData(self):
        print('Account DNI:',self.dni)
        print('Account Balance:',self.balance)
        print('Annual Interest:',self.annualInterest)
        print('Account Number:',self.accountNumber)

if __name__ == '__main__':
    pablo = Account()
    pablo.updateBalance()
    pablo.inputMoney(300)
    pablo.removeMoney(150)
    pablo.getData() 