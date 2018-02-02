bill = float(raw_input('Total bill amount? '))
service = raw_input('Level of service? ')
split = int(raw_input('Split how many ways? '))
if service == 'good': 
  tip = 0.2
elif service == 'fair':
  tip = 0.15
elif service == 'bad':
  tip = 0.1



print """Tip amount: $%d
Total amount: $%d 
Amount per person: $%.2f""" % (bill * tip, bill * (1+ tip), bill*(1+tip)/split)

