m1 = [
[2, 3],
[1, 4]]
m2 = [
[0, -2],
[9, 4]]
cor_answer =[
[27, 8],
[36, 14]
]
new_ls = []

for i in range(0, len(m1)):
  for j in range(0, len(m1[i])):
    if j == 0:
      new_ls.append([m1[i][j]* m2[i][j] + m1[i][j+1]*m2[i+1][j+1]])