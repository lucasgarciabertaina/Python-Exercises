""" 
Cargar una lista con números. Invertir los 
elementos sin usar otra lista. 
"""

numbers = [1, 2, 3, 4, 5, 6]
j = 1
for number in range(len(numbers)-1, 0, -1):
    numbers.append(numbers[number]-j)
    del numbers[0]
    j = j + 1

print(numbers)
