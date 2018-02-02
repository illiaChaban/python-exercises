start = int(raw_input('Number to start? '))
end = int(raw_input('Number to end? '))
if end < start:
  print 'error'
else:
  for i in range(start, end + 1):
    print i