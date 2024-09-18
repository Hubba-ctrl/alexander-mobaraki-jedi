import math 
def square_digits(num):
    result = [] 
    for digit in str(num):
        processed = int(digit) ** 2
        result.append(str(processed))
    return int("".join(result))
input_numbers = int(input("enter your numbers: "))
output = square_digits(input_numbers) 
print(output)