to_open = 'lorem.txt'
f = open(to_open)
all_letters = {}
for line in f:
  for ch in line:
    ch = ch.lower()
    if ch.isalpha():
      if ch not in all_letters:
        all_letters[ch] = 1
      else:
        all_letters[ch] = all_letters[ch] + 1
f.close()

for key in sorted(all_letters):
  print("%s: %s" % (key, all_letters[key]))
