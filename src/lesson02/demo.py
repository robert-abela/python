age = input('What is your age? ')
age_as_num = int(age)
next_age = age_as_num+1
print("next year you'll be "+str(next_age))

n1 = input('Enter num 1: ')
n1 = int(n1)
n2 = input('Enter num 2: ')
n2 = int(n2)
total = n1+n2
print(total)

weight = input('The weight of a person ')
weight = float(wieght)

f = 9.3 / 6.1
print("%.2f" % f)

import datetime
time = datetime.datetime.now()
print(time)

pixel = {'name': 'Pixel', 'weight': 6.0, 'color': 'ginger', 'gender': 'M'}
pixel['weight'] = 6.1
pixel['favfood'] = 'chicken'
print(pixel)

car = {}
atr = input('attribute 1: ')
val = input('value 1:     ')
car[atr] = val
atr = input('attribute 2: ')
val = input('value 2:     ')
car[atr] = val
atr = input('attribute 3: ')
val = input('value 3:     ')
car[atr] = val
print(car)
