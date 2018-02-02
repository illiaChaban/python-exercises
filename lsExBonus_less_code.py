#lsBonus

m1 = [
[2, 3],
[1, 4],
[3, 5],
[4, -2]
]
m2 = [
[0, -2, 3],
[9, 4, 6]
]


new_m1 = []

for y in range(0, len(m1)):
  for i in range(0, len(m1)):
    for j in range(0, len(m2[i])):
      if y == 0 and j == 0:
        new_m1.append([m1[i][y]* m2[y][j]])
      elif y == 0:
        new_m1[i].append(m1[i][y]* m2[y][j])
      else: 
        new_m1[i][j] += m1[i][y]* m2[y][j]
for x in new_m1:
    print x


