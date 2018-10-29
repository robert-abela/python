# 0, 2, ..., 96, 98
for counter in range(0, 100, 2): #start, stop-1, step
   print(counter)

# 99, 97, ..., 3, 1
for counter in range(99, 0, -2): #start, stop-1, step
   print(counter)

print('test'.startswith('t'))
print('testing'.endswith('g'))
print('Hello'.islower())
print('BYE'.isupper())
print('BYE'.lower())
print('Home'.upper())
print('My phone is 79797979'.isalpha())
print('ABC132'.isdigit())
print('i am Robert'.swapcase())
print('hello. i am robert'.title())
print(len('Istanbul'))

stars = ''
for cnt in range(1, 8):
    stars = stars + '*'
    print(stars)
