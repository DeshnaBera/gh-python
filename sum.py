import sys

def add_numbers(a, b):
    return a + b

if len(sys.argv) == 3:
        num1 = 4
        num2 = 5
        result = add_numbers(num1, num2)
        print(result)