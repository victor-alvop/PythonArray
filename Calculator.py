# calculator

def suma(x,y):
    return print(x+y)

def resta(x,y):
    return print(x-y)

def multiplicacion(x,y):
    return print(x*y)

def division(x,y):
    return print(x/y)

option2 = 0

while option2 != 5:

    print(' ')
    print('**************************')
    print('CALCULATOR')
    print('Choose an option')
    print('1 - Suma')
    print('2 - Resta')
    print('3 - Multiplicacion')
    print('4 - Division')
    print('5 - Exit')
    option2 = int(input('Choose an option: '))
    

    if option2 == 1:
        number1 = float(input('Enter a number: '))
        number2 = float(input('Enter a number: '))
        suma(number1, number2)
    elif option2 == 2: 
        number1 = float(input('Enter a number: '))
        number2 = float(input('Enter a number: '))
        resta(number1, number2)
    elif option2 == 3: 
        number1 = float(input('Enter a number: '))
        number2 = float(input('Enter a number: '))
        multiplicacion(number1, number2)
    elif option2==4:
        number1 = float(input('Enter a number: '))
        number2 = float(input('Enter a number: '))
        division(number1, number2)