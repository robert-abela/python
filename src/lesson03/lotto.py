import random
random.random()

#n1 = random.randint(1,90)
#n2 = random.randint(1,90)
#n3 = random.randint(1,90)
#n4 = random.randint(1,90)
#n5 = random.randint(1,90)
#print('Lotto results:', n1, n2, n3, n4, n5)

#result = []
#result.append(random.randint(1,90))
#result.append(random.randint(1,90))
#result.append(random.randint(1,90))
#result.append(random.randint(1,90))
#result.append(random.randint(1,90))
#print('Lotto results:', result)

#result = []
#for i in range(5):
#    result.append(random.randint(1,90))
#print('Lotto results:', result)

result = []
while len(result) < 5:
    new_num = random.randint(1,90)
    if new_num not in result:
        result.append(new_num)

print('Lotto results:', result)
