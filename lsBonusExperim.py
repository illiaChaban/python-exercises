#lsBonus
#experiment
#I will create 2 matrices and add them
# devide the operation by 2

m1 = [
[2, 3],
[1, 4]]
m2 = [
[0, -2, 3],
[9, 4, 6]
]
# correct answer
# 	C1	C2	C3
# 	27	8	24
# 	36	14	27
new_ls = []
new_m1 = []
new_m2 = []

#creating 1st matrix
for i in range(0, len(m1)):
  for j in range(0, len(m2[i])):
    if j == 0:
      new_m1.append([m1[i][0]* m2[0][j]])
    else:
      new_m1[i].append(m1[i][0]* m2[0][j])

#creating 2nd matrix
for i in range(0, len(m1)):
  for j in range(0, len(m2[i])):
    if j == 0:
      new_m2.append([m1[i][1]* m2[1][j]])
    else:
      new_m2[i].append(m1[i][1]* m2[1][j])

print new_m1
print new_m2

#adding both matrix
for i in range(0, len(new_m1)):
  for j in range(0, len(new_m2[1])):
    # new_ls[i][j] = ls1[i][j] + ls2[i][j]
    if j == 0:
        new_ls.append([new_m1[i][j] + new_m2[i][j]])
    else:
        new_ls[i].append(new_m1[i][j] + new_m2[i][j])
for x in new_ls:
    print x