import sys

def add_numbers(a, b):
    return a + b

if len(sys.argv) == 3:
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        result = add_numbers(num1, num)
        print(result)
    except Exception as e:
        sys.exit(1)
    else:
        sys.exit(0)