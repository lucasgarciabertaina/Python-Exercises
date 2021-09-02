# The numeric system represented by Roman numerals originated in ancient Rome and remained
# the usual way of writing numbers throughout Europe well into the Late Middle Ages.
# Roman numerals, as used today, employ seven symbols, each with a fixed integer value.

# See the below table the Symbol - Value pairs:

# I - 1
# V - 5
# X - 10
# L - 50
# C - 100
# D - 500
# M - 1000
# User Stories
#  User should be able to enter one Roman number in an input field
#  User could see the results in a single output field containing the decimal (base 10)
#  equivalent of the roman number that was entered by pressing a button
#  If a wrong symbol is entered, the User should see an error
romanNumbers = {'I': 1, 'V': 5, 'X': 10,
                'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def correctCharacter(inputRoman):
    letters = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    for i in inputRoman:
        control = True
        for j in letters:
            if i == j:
                control = False
        if control:
            return True
    return False


def correctQuantity(inputRoman):
    for i in range(len(inputRoman)):
        if inputRoman.count(inputRoman[i]) > 3:
            return True
        elif inputRoman.count(inputRoman[i]) == 2:
            position = inputRoman.index(inputRoman[i])
            if inputRoman[position] != inputRoman[position+1]:
                return True
        elif inputRoman.count(inputRoman[i]) == 3:
            position = inputRoman.index(inputRoman[i])
            if inputRoman[position] != inputRoman[position+1] or inputRoman[position] != inputRoman[position+2]:
                return True
    return False


def inputNumber():
    romanRomanNumber = input('Please input the number: ').upper()
    while correctQuantity(romanRomanNumber) or correctCharacter(romanRomanNumber):
        print(romanRomanNumber)
        romanRomanNumber = input(
            'Incorrect Roman Number\nPlease input the number: ').upper()
    return romanRomanNumber


def romanDecimal():
    roman = inputNumber()
    total = 0
    for i in range(len(roman)):
        if roman[i] == 'I':
            times = roman.count(roman[i])
            if i < len(roman)-1 and i != 0:
                if roman[i+1] == 'V' or roman[i+1] == 'X' or roman[i+1] == 'L' or roman[i+1] == 'C' or roman[i+1] == 'D' or roman[i+1] == 'M':
                    times = roman.count(roman[i])
                    for i in range(times):
                        total -= romanNumbers['I']
                        i += 1
                elif roman[i-1] == 'V' or roman[i-1] == 'X' or roman[i-1] == 'L' or roman[i-1] == 'C' or roman[i-1] == 'D' or roman[i-1] == 'M':
                    for i in range(times):
                        total += romanNumbers['I']
                        i += times-1
            elif i == 0 and i < len(roman)-1:
                if roman[i+1] == 'V' or roman[i+1] == 'X' or roman[i+1] == 'L' or roman[i+1] == 'C' or roman[i+1] == 'D' or roman[i+1] == 'M':
                    times = roman.count(roman[i])
                    for i in range(times):
                        total -= romanNumbers['I']
                        i += 1
                elif roman[i+1] == 'I':
                    times = roman.count(roman[i])
                    for i in range(times):
                        total += romanNumbers['I']
                        i += times-1
            elif len(roman) == 1:
                total += romanNumbers['I']
            else:
                if roman[i-1] == 'V' or roman[i-1] == 'X' or roman[i-1] == 'L' or roman[i-1] == 'C' or roman[i-1] == 'D' or roman[i-1] == 'M':
                    for i in range(times):
                        total += romanNumbers['I']
                        i += times-1
        elif roman[i] == 'V':
            if i < len(roman)-1 and i != 0:
                if roman[i+1] == 'X' or roman[i+1] == 'L' or roman[i+1] == 'C' or roman[i+1] == 'D' or roman[i+1] == 'M':
                    times = roman.count(roman[i])
                    for i in range(times):
                        total -= romanNumbers['V']
                        i += 1
                elif roman[i-1] == 'I' or roman[i-1] == 'X' or roman[i-1] == 'L' or roman[i-1] == 'C' or roman[i-1] == 'D' or roman[i-1] == 'M':
                    for i in range(times):
                        total += romanNumbers['V']
                        i += times-1
            elif i == 0 and i < len(roman)-1:
                if roman[i+1] == 'X' or roman[i+1] == 'L' or roman[i+1] == 'C' or roman[i+1] == 'D' or roman[i+1] == 'M':
                    times = roman.count(roman[i])
                    for i in range(times):
                        total -= romanNumbers['V']
                        i += 1
                elif roman[i+1] == 'I':
                    times = roman.count(roman[i])
                    for i in range(times):
                        total += romanNumbers['V']
                        i += 1
                elif roman[i+1] == 'V':
                    times = roman.count(roman[i])
                    for i in range(times):
                        total += romanNumbers['V']
                        i += times-1
            elif len(roman) == 1:
                total += romanNumbers['V']
            else:
                if roman[i-1] == 'I' or roman[i-1] == 'X' or roman[i-1] == 'L' or roman[i-1] == 'C' or roman[i-1] == 'D' or roman[i-1] == 'M':
                    for i in range(times):
                        total += romanNumbers['V']
                        i += times-1
        elif roman[i] == 'X':
            if i < len(roman)-1 and i != 0:
                if roman[i+1] == 'L' or roman[i+1] == 'C' or roman[i+1] == 'D' or roman[i+1] == 'M':
                    times = roman.count(roman[i])
                    for i in range(times):
                        total -= romanNumbers['X']
                        i += 1
                elif roman[i-1] == 'I' or roman[i-1] == 'V' or roman[i-1] == 'L' or roman[i-1] == 'C' or roman[i-1] == 'D' or roman[i-1] == 'M':
                    for i in range(times):
                        total += romanNumbers['X']
                        i += times-1
            elif i == 0 and i < len(roman)-1:
                if roman[i+1] == 'L' or roman[i+1] == 'C' or roman[i+1] == 'D' or roman[i+1] == 'M':
                    times = roman.count(roman[i])
                    for i in range(times):
                        total -= romanNumbers['X']
                        i += 1
                elif roman[i+1] == 'I' or roman[i+1] == 'V':
                    times = roman.count(roman[i])
                    for i in range(times):
                        total += romanNumbers['X']
                        i += 1
                elif roman[i+1] == 'X':
                    times = roman.count(roman[i])
                    for i in range(times):
                        total += romanNumbers['X']
                        i += 1
            elif len(roman) == 1:
                total += romanNumbers['X']
            else:
                if roman[i-1] == 'I' or roman[i-1] == 'V' or roman[i-1] == 'L' or roman[i-1] == 'C' or roman[i-1] == 'D' or roman[i-1] == 'M':
                    for i in range(times):
                        total += romanNumbers['X']
                        i += times-1
    print(total)


def main():
    romanDecimal()


if __name__ == '__main__':
    main()
