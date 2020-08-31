to_open = 'lorem.txt'
f = open(to_open)
counter = 0
for line in f:
  counter+=1
  if counter % 2 == 1:
    print(line)
f.close()

## Done during lesson 31.08.2020

try:
	to_open = 'lorem.txt'
	f = open(to_open)
	print_line = True
	for line in f:
		if print_line == True:
			print(line)
		print_line = not print_line
	f.close()
except IOError:
	print("Error")