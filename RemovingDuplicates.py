def removeDuplicates(array):
    no_duplicates_array = set(array)
    if len(array) == len(no_duplicates_array):
        print('There is no duplicates')
    else:
        print(f'Duplicates removed {no_duplicates_array}')

default_array = [1,2,3,4,3]

removeDuplicates(default_array)

