# ls = [4, 5, -8, 4, 6, 9, 0, -1 ,17]
# for i in ls:
#   if i > 0:
#     print i

ls1 = [4, 5, -8, 4, 6, 9, 0, -1 ,17]

def positive(ls):
  new_ls = []
  for i in ls:
    
    if i > 0:
      new_ls.append(i)
  return new_ls
  
print positive(ls1)