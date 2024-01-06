default_array = []

while True: 
    value = input('Enter a number: ')
    if value == 'done': break
    else:
        value = int(value)
        default_array.append(value)

default_array_copy = list(default_array)
default_array_copy.remove(max(default_array))

first_max_number = max(default_array)
second_max_number = max(default_array_copy)
max_product = first_max_number * second_max_number

print(f'The max product is {first_max_number} * {second_max_number} = {max_product} ')


