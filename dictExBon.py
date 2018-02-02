#dict bonus

# sentence = raw_input('Your sentence: ')
sentence = 'to or or to be or not to be or to be or not i don\'t know'
new_dic = {}
for i in sentence.lower().split():
    count = 0
    for j in sentence.lower().split():
        
        if i == j:
            count +=1
    new_dic[i] = count

tuples = new_dic.items()
sort_tuples = sorted(tuples , key = lambda x: x[1])
for i in range(1, 4):
    print "%s: %d" %(sort_tuples[len(sort_tuples) - i][0], sort_tuples[len(sort_tuples) - i][1])