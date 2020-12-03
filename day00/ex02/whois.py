import sys

if len(sys.argv) != 2:
    print('ERROR')
    exit()
try:
    numb = int(sys.argv[1])
except ValueError:
    print('ERROR')
    exit()
if numb == 0:
    print("I'm Zero.")
elif numb % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
