"""
Ingresar 7 números enteros y en el caso de que
sean naturales de una sola cifra mostrar un
cartel en cada uno.
"""

conditionList = []
for i in range(7):
    number = int(input('Insert a number: '))
    if number >= 0 and number < 10:
        conditionList.append(number)

for j in range(0, len(conditionList)):
    print(conditionList[j])
