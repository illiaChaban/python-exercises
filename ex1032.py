day = int(raw_input('Day (0-6)? '))
# Don't use | in python.
if day == 0 | 6:
  day = "Sleep in"
elif day in range(1, 6):
  day = "Go to work"
else: 
  day = "error"

print day