import array 
import random 

# 1. create an array and traverse
def CreateArray(array):
    print(f'Original: {array}')
    for index, element in enumerate(my_array_random01):
        array[index] = element + 1
    
    print(f'Original + 1: {array}')

# 2. Access an individual 
def AcessIndividual(array, index):
    return print(array[index-1])

# 3. append any value to array
def AppendValue(array, value):
    array.append(value)

# 4. insert value in array
def InsertValue(array, index, value):
    array.insert(index, value)

# 6. remove any array element 
def RemoveAny(array, index):
    array.pop(index)

# 7. remove last array element
def RemoveLastElement(array):
    array.pop()

# 8. fetch any array using index 
def FetchByIndex(array, index):
    return print(array[index-1])

# 9. reverse de python array 
def ReverseArray(array):
    array.reverse()
    return print(array)

# 10. check the ocurriencies of an element
def CountOcurrencies(array, element):
    return print(array.count(element))

# 11. convert an array to string 
def ConvertToString(array):
    delimiter = ', '
    string_array = delimiter.join(map(str, array))
    return print(type(string_array), string_array)

# 12. slice elements from an array
def SliceArray(array, start_index, end_index):
    sliced_array = array[start_index-1:end_index]
    return print(sliced_array)

user_option = 100
my_array_random01 = [random.randint(1, 1009) for _ in range(25)]

print(f'Default array is: {my_array_random01}')

while user_option != 0: 

    print('\n1. traverse array')
    print('2. access individual elements through indexes')
    print('3. append any value to array')
    print('4. insert value in array')
    print('5. extend an array')
    print('6. remove any array element')
    print('7. remove last array element')
    print('8. fetch any array using index')
    print('9. reverse de python array')
    print('10. check the ocurriencies of an element')
    print('11. convert an array to string')
    print('12. slice elements from an array')
    user_option = int(input('Choose an option: '))
    
    
    if user_option == 1:
        CreateArray(my_array_random01)

    elif user_option == 2: 
        index_user = int(input('Select the index you want to access: '))
        AcessIndividual(my_array_random01, index_user)

    elif user_option == 3:
        value_to_append = int(input('Enter a value: '))
        AppendValue(my_array_random01, value_to_append)
        print(f'The new array is: {my_array_random01}')

    elif user_option == 4: 
        value_to_insert = int(input('Enter a value: '))
        position_to_insert = int(input('Enter the position: '))
        position_to_insert -= 1
        InsertValue(my_array_random01, position_to_insert, value_to_insert)
        print(f'The new array is: {my_array_random01}')

    elif user_option == 5: 
        number_to_add_extend = 0
        array_to_extend = []
        index_iterator = 0
        stop_extend_list = '-'

        while stop_extend_list != '*':
            stop_extend_list = input('To add the current list press * if you want to keep adding numbers press another key')
            if stop_extend_list == '*': break

            number_to_add_extend = int(input('Enter a number to add the list: '))
            array_to_extend.insert(index_iterator, number_to_add_extend)
            index_iterator += 1
            print(f'The array is you will use to extend is: {array_to_extend}')

        my_array_random01.extend(array_to_extend)
        print(f'The array extended is: {my_array_random01}')
        print(f'You added {index_iterator}')
    elif user_option == 6:
        index_remove = int(input('Enter the index you want to delete: '))
        print(f'The element {my_array_random01[index_remove-1]} element will be removed from default array')
        RemoveAny(my_array_random01, index_remove-1)
        print(my_array_random01)
    elif user_option == 7: 
        RemoveLastElement(my_array_random01)
        print(f'The element {my_array_random01[-1]} will be removed')
        print(f'The new array is: {my_array_random01}')
    elif user_option == 8: 
        fetch_index = int(input('Enter the index you want to look for: '))
        FetchByIndex(my_array_random01, fetch_index)
    elif user_option == 9:
        ReverseArray(my_array_random01)
    elif user_option == 10:
        element_to_count = int(input('Enter the element: '))
        CountOcurrencies(my_array_random01, element_to_count)
    elif user_option == 11:
        ConvertToString(my_array_random01)
    elif user_option == 12: 
        start_index = int(input('Enter the start number: '))
        end_index = int(input('Enter the end number: '))
        SliceArray(my_array_random01, start_index, end_index)
