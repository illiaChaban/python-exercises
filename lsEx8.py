# ls1 = [4, 5, -8]
# ls2 = [2, 0, 3]
# new_ls = []
# for i in range(0, len(ls1)):
#   new_ls.append(ls1[i] * ls2[i])
# print new_ls
  
ls1 = [4, 5, -8]
ls2 = [2, 0, 3]

def multiply_vector(lst1, lst2):
    new_ls = []
    for i in range(0, len(lst1)):
        new_ls.append(lst1[i] * lst2[i])
    return new_ls
  
print multiply_vector(ls1, ls2)