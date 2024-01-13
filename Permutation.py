def perumation(array_1, array_2): 
    if len(array_1) != len(array_2): return False 
    array_1.sort()
    array_2.sort()
    return True if array_1 == array_2 else False 


default_array_1 = [1,2,3,4]
default_array_2 = [4,3,2,1]

print(perumation(default_array_1, default_array_2))