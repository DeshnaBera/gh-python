import sys

def add_numbers(a, b):
    return a + b

if len(sys.argv) == 3:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        result = add_numbers(num, num2)
        print(result)