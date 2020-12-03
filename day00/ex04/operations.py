import sys

usage = "\n\nUsage: python operations.py <number1> <number2>"
example = "\nExample:\n\tpython operations.py 10 3"
if len(sys.argv) < 3:
    print("InputError: too few arguments", usage, example)
    exit()
elif len(sys.argv) > 3:
    print("InputError: too many arguments", usage, example)
    exit()
try:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
except ValueError:
    print("InputError: only numbers", usage, example)
    exit()
print("Sum:\t\t{0}".format(num1+num2))
print("Difference:\t{0}".format(num1-num2))
print("Product:\t{0}".format(num1*num2))
if num2 != 0:
    print("Quotient:\t{0}".format(num1/num2))
    print("Remainder:\t{0}".format(num1 % num2))
else:
    print("Quotient:\tERROR (div by zero)")
    print("Remainder:\tERROR (modulo by zero)")
