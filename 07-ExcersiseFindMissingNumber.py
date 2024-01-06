def find_mising_number(arr, n):
    excpected_sum = n * (n+1) / 2
    actual_sum = sum(arr)
    missing_number = excpected_sum - actual_sum
    return print(missing_number)

default_array = [1,2,3,4,5,7]
elements_in_array = 7

find_mising_number(default_array, elements_in_array)

