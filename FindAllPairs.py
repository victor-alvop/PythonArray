'''
Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.
Example
pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
Output : ['2+5', '4+3', '3+4', '-2+9']
'''

def pairSum(array, target):

    result = []
    seen_numbers = set()

    for num in array:
        complement = target - num 
        if complement in  seen_numbers:
            pair_sum = (complement, num)
            pair_sum_str = (f'{pair_sum[0]} + {pair_sum[1]}')
            result.append(pair_sum_str)

        seen_numbers.add(num)
    
    return result

default_array = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
default_target = 7
print(pairSum(default_array, default_target))


