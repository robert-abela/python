#Declarations
myInteger = 77
print(myInteger)

myFloat = 77.7
print(myFloat)

rounded = int(myFloat)
print(rounded)

aString = 'Here is a string'
print(aString)
anotherString = "Here's another one"
print(anotherString)
complexString = '''This string has a single (') and a double (") quote.'''
print(complexString)

# Adding variables

one = 1
ten = 15 - 5
eleven = one + ten
print(eleven)

createdBy = "Python was created by"
guido = "Guido van Rossum"
sentence = createdBy + " " + guido
print(sentence)

seven = 7
twoAndHalf = 2.5
hello = "hello"

# This will work!
print(seven, twoAndHalf, hello)

# This will not work!
# print(seven + twoAndHalf + hello)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

#Fix 
print(str(seven) + str(twoAndHalf) + hello)

# Formatted strings
print("Integer: %d" % seven)
print("Float: %f" % twoAndHalf)
print("String: %s" % hello)

print("%d %.2f %s" % (seven, twoAndHalf, hello))
