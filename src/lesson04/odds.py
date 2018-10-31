def odds(items):
  filtered = []
  use_this_item = True
  for item in items:
    if use_this_item:
      filtered.append(item)
    use_this_item = not use_this_item
  
  return filtered
  
print(odds(['a', 'b', 'c', 'd', 'e']))
