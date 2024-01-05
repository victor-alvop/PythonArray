temperature_list = []
value = 0

while True:
    value = input('Enter a temperature: ')
    if value == 'done': break 
    else: 
        value = float(value)
        temperature_list.append(value)

average_temperature = sum(temperature_list)/len(temperature_list)
over_average_temperature = [number for number in temperature_list if number > average_temperature]

print(f'The average temperature is: {average_temperature}')
print(f'This temperatures are over the average {over_average_temperature}')


