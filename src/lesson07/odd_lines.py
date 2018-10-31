to_open = 'lorem.txt'
f = open(to_open)
counter = 0
for line in f:
  counter+=1
  if counter % 2 == 1:
    print(line)
f.close()
