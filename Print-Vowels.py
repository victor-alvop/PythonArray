# a console program that can print all the vowels in word
def vowels(function_word_variable):
    return [print(element) for element in function_word_variable if element == 'a' or element == 'e' or element == 'i' or element == 'o' or element == 'i']

user_word = input('Enter a word: ')
vowels(user_word)