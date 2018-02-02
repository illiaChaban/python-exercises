reverse = raw_input('What string would you like to reverse? ')
l = ''
for i in range(len(reverse)-1, -1, -1):
  l += reverse[i]
print l