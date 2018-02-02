x = int(raw_input('What number do you want to start counting from? '))
import time
if x > 20:
    print 'error'
else:
  for i in range(x, -1, -1):
    print i
    time.sleep(1)
    
  print "we are done"