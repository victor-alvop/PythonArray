# this is console program where you can add numbers to an array, print them and access specific positions

import array 

my_array3 = array.array('i')
opcion1 = 1 

def add_element(x):
    my_array3.append(x)

def show():
    return print(f'Tu arreglo es: {my_array3}')

def access_element(element):
    return print('The element in the position is: ', my_array3[element-1])

while opcion1 != 0:  

    print(' ')
    print('-- Please declare the array --')
    print('Press 0 to skip')
    print('Press 1 to add a number')
    print('Press 2 to show array')
    print('Press 3 to access a position in the array')

    opcion1 = int(input('Enter an option: '))

    if opcion1 == 0:
        break
    elif opcion1 == 1:
        number1 = int(input('Enter the number tu add: '))
        add_element(number1)
    elif opcion1 == 2:
        show()
    elif opcion1 == 3:
        access_user_number = int(input('Enter the position number: '))
        access_element(access_user_number)