string = raw_input('String to extend: ')
vowels = 'aoeui'
new_str = ''
for i in string:
  if i.lower() in vowels:
    new_str += i*5
  else: 
    new_str += i
print new_str
    