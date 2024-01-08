'''
Given a list, write a function to get first, second best scores from the list.
List may contain duplicates.
Example
myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
first_second(myList) # 90 87
'''
import random

def bestScores(array):
    if len(array) < 2:
        return 'Not enough data'

    sorted_scores = sorted(array, reverse=True) 
    first_score = sorted_scores[0]
    second_score = sorted_scores[1]

    return print(f'The best scores are {first_score}, {second_score}')

default_array = [random.randint(1,100) for element in range(10)]
print(f'Default array: {default_array}')

bestScores(default_array)
