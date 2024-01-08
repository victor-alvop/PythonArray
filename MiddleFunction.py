'''
Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
myList = [1, 2, 3, 4]
middle(myList)  # [2,3]
'''

import random 

default_array =  [random.randint(1,100) for number in range(10)]
print(f'Default array: {default_array}')

def middleFunction(array):
    new_array = [element for element in array]
    new_array.pop(0)
    new_array.pop()
    print(new_array)

middleFunction(default_array)