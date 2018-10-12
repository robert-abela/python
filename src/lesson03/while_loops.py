# You are to write scripts as requested below using the while loops:

# ask the user to enter 5 numbers and print the total at the end. 

count = 0
total = 0
while count < 5:
    num = input('Enter a number: ')
    total += int(num)
    count += 1

print('Total is', total)

# print out the the shape below
# *
# **
# ***
# ****
# *****
# ******
#
count = 1
while count < 7:
    print('*'*count)
    count += 1
     
# ask the user to enter 3 names and print the longest
longest_name = ''
count = 0
while count < 3:
    name = input('Enter a name: ')
    if len(name) > len(longest_name):
        longest_name = name
    count += 1
print('Longest name is: ', longest_name)