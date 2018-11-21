import sys

if len(sys.argv) < 4:
    print('there are some missing parameters')
    exit(1)
try:
    n1 = int(sys.argv[1])
    sign = sys.argv[2]
    n2 = int(sys.argv[3])
except ValueError:
    print('there are some invalid number')
    exit(2)
else:
    if sign == '+':
        print(n1+n2)
    elif sign == '-':
        print(n1-n2)
    else:
        print('invalid sign')
        exit(3)
