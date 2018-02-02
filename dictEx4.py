#word_histogram
sentence = raw_input('Your sentence: ')
new_dic = {}
for i in sentence.lower().split():
    count = 0
    for j in sentence.lower().split():
        
        if i == j:
            count +=1
    new_dic[i] = count

print new_dic
