three_dig_number = input("Enter a 3 digit number and i'll give you back the sum! Enter here: ")

first = three_dig_number[0]
second = three_dig_number[1]
third = three_dig_number[2]

sum = int(first) + int(second) + int(third)

print(f'The sum of the digits of {three_dig_number} is {sum}')


