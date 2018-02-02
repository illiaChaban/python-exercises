# ls1 = [[4, 5, -8],
# [3, 2, 9]]
# ls2 = [[2, 0, 3],
# [-2, -4, 0]]
# new_ls = [[0,0,0],[0,0,0]]

# for i in range(0, len(ls1)):
#   for j in range(0, len(ls1[1])):
#     new_ls[i][j] = ls1[i][j] + ls2[i][j]
# print new_ls
  
ls1 = [
[4, 5, -8],
[3, 2, 9],
[3, 0, -2]]
ls2 = [
[2, 0, 3],
[-2, -4, 0],
[2, 2, 1]]


# for i in range(0, len(ls1)):
#   for j in range(0, len(ls1[1])):
#     
#     if j == 0:
#         new_ls.append([ls1[i][j] + ls2[i][j]])
#     else:
#         new_ls[i].append(ls1[i][j] + ls2[i][j])
# for x in new_ls:
#     print x

def add_matrixes(lst1, lst2):
    new_ls = []
    for i in range(0, len(lst1)):
        new_ls.append([])
        for j in range(0, len(lst1[1])):
                new_ls[i].append(lst1[i][j] + lst2[i][j])
    return new_ls
  
print add_matrixes(ls1, ls2)