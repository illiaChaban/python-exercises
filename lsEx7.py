# ls = [4, 5, -8, 4, 6, 9, 0, -1 ,17]
# factor = 5
# new_ls = []
# for i in ls:
#   new_ls.append(i * factor)
# print new_ls

ls1 = [4, 5, -8, 4, 6, 9, 0, -1 ,17]
factor1 = 5

def multiply_by_factor(ls, factor):
  new_ls = []
  for i in ls:
    new_ls.append(i * factor)
  return new_ls

print multiply_by_factor(ls1, factor1)