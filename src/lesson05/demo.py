
#Task
#Write a function that asks the user to enter a number and returns it.
#Use a loop and exception handling to make sure that a number is
#actually entered.
#Hint: ValueError is raised when casting a string to an int fails.


def input_idcard(msg):
    while True:
        idcard = input(msg)
        lastchar = idcard[-1]
        num = idcard[0:-1]
        
        if lastchar not in 'ABGHLMPZ':
            print('wrong ending')
            continue

        try:
            int(num)
        except ValueError:
            print("wrong number")
        else:
            return idcard


def input_number(msg):
    '''Reads from user until a valid number.

       Takes a string as an argument to show to the user. will
       repeat user input until a valid integer is entered. Finally
       it will return the int'''
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Try again")

#print(input_number.__doc__)

#ret_value = input_number('Enter your salary:')
#print(ret_value)
#ret_value = input_number('Enter your age:')
#print(ret_value)

ret_value = input_idcard('Enter IDCard number: ')
print(ret_value)

