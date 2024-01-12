'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Example :
Input: nums = [1,2,3,1]
Output: true
'''

def containsDuplicate(array): 
    no_duplicates = set(number for number in array)
    return False if len(array) == len(no_duplicates) else True

default_arrray = [1,2,4,4,5,6,5,6,7,2]
test_array = [1,2,3,4,5,6,7]

print (f'Contains duplicates -> {containsDuplicate(default_arrray)}')