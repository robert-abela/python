def print_solid_box(height, width):
  '''
  Prints a solid box shape made up of '*'
  '''
  for lines in range(height):
    print('*' * width)

def print_hollow_box(height, width):
  '''
  Prints a hollow box shape made up of '*'
  '''
  print('*' * width)
  for lines in range(height-2):
    print('*' + ' '*(width-2) + '*')
  print('*' * width)

def print_triangle(height):
  '''
  Prints a solid triangle shape made up of '*'
  '''
  lines = 0
  for counter in range(1, height+1):
    indent = height - counter
    stars = (counter*2)-1
    line = (' ' * indent) + ('*' * stars)
    print(line)