def average(nums):
  total = 0
  for n in nums:
    total += n
  return total / float(len(nums))

print("%.2f" % average([9,9,10]))
