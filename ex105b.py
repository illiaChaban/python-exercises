width = int(raw_input('Width? '))
height = int(raw_input('Height? '))
print '*' * width
for i in range(0, height - 2):
  print "*" + " "*(width - 2) + "*"
print '*' * width