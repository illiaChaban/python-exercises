# i = 0
# while i < 4:
#   i += 1
#   print '*' * i
# levels = int(raw_input('How many levels do you want in your triangle? '))
# for i in range(1, levels+1):
#     print ' '*((2*(levels - i+1) - 2)/2) + '*'*(2*i -1) + ' '*((2*(levels - i +1) -2)/2)
levels = int(raw_input('How many levels do you want in your triangle? '))
for i in range(1, levels+1):
    spaces_at_each_end = ' '*((2*(levels - i+1) - 2)/2)
    middle = '*'*(2*i -1)
    print spaces_at_each_end + middle