

def add_two_numbers(a, b):
    return a + b



def subtract_two_numbers(a, b):
    return a - b


def multiply_two_numbers(a, b):
    return a * b

def divide_two_numbers(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    else:
        return a / b




num1 = 5
num2 = 3
result = add_two_numbers(num1, num2)
result1 = subtract_two_numbers(num1, num2)
result2 = multiply_two_numbers(num1, num2)
result3 = divide_two_numbers(num1, num2)

print(f"The sum of {num1} and {num2} is: {result}")
print(f"The difference of {num1} and {num2} is: {result1}")
print(f"The product of {num1} and {num2} is:{result2}")
print(f"The divide of {num1} and {num2} is:{result3}")