# ls = [4, 5, 4, 6, 9, 0]
# for i in ls:
#   if i % 2 == 0:
#     print i

ls1 = [4, 5, 4, 6, 9, 0]
def even(ls):
  new_ls = []  
  for i in ls:
    if i % 2 == 0:
      new_ls.append(i)
  return new_ls
    
print even(ls1)
    