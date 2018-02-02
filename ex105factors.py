#factors
list_of_factors = []
number = int(raw_input('Number? '))
if number <= 1:
  print 'error. Choose another number'
else:
  for i in range(2, number+1):
    if number % i == 0:
      list_of_factors.append(i)
if len(list_of_factors) == 1:
    print "It's a prime!!!"
else:
    print list_of_factors