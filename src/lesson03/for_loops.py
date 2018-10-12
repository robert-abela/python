# You are to write scripts as requested below using the for loops:

# ask the user to enter 5 numbers and print the total at the end. 

total = 0
for count in range(5):
    num = input('Enter a number: ')
    total += int(num)

print('Total is', total)

# print out the the shape below
# *
# **
# ***
# ****
# *****
# ******
#

for starts in range(1, 8):
    print('*'*starts)
     
# ask the user to enter 3 names and print the longest
longest_name = ''
for count in range(3):
    name = input('Enter a name: ')
    if len(name) > len(longest_name):
        longest_name = name

print('Longest name is: ', longest_name)