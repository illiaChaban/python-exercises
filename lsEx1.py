# ls = [4, 5]
# sum = 0
# for i in ls:
#   sum += i
# print sum

def sum(ls):
  sum = 0
  for i in ls:
    sum += i
  return sum

print sum([3, 2, 4])