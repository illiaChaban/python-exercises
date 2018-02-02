print 'You have 0 coins'
answer = raw_input('Do you want another? ')
coins = 0

while answer == 'yes':
  coins += 1
  print 'You have %d coins' % coins
  answer = raw_input('Do you want another? ')
print 'Bye'  
  
  
  