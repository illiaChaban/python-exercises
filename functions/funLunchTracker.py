# Lunch Tracker

restaurants = {
    1: 'Chipotle',
    2: 'Chick fil a',
    3: 'Ramen stuff'}

list_of_choices = {
    1: 0,
    2: 0,
    3: 0
}
#while loop?    
for i in range(5):
    choice_num = int(raw_input("""hi, choose 1 of the restaurants:
_ 1 for Chipotle
_ 2 for Chick fil a
_ 3 for Ramen stuff: """))
    list_of_choices(choice_num)
    if choice_num == 0:
        break

    elif 
    print "you chose %s!" % restaurants[choice_num]
    