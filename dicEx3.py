sentence = raw_input('Please enter a sentence: ')
dic = {}
for i in sentence:
  count = 0
  for j in sentence:
    if i == ' ':
      break
    elif i == j:
      count +=1
    dic[i] = count
print dic