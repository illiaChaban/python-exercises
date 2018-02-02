

# print '''Please fill in the blanks below:'''
# string1 = '''___(name)___'s favorite subject in school is ___(subject)___.'''
# print string1
# # name1 = raw_input('What is your name?')
# # subject1 = raw_input('What is your favorite subject?')

# def mad_lib(string, name, subject):
#     str_spl = string.split()
#     for i in str_spl:
#         if "___" in i:
#             index = str_spl.index(i)
#             str_spl[index] = '%s' 
#     return ' '.join(str_spl) % (name, subject)        
    

# print mad_lib("___(name)___'s favorite subject in school is ___(subject)___.", 'josh', 'ballet')
# # add prompting a user about filling the blanks no matter how many blanks it has




print '''Please fill in the blanks below:'''
string1 = '''___(name)___'s favorite subject in school is ___(subject)___.'''
print string1
# name1 = raw_input('What is your name?')
# subject1 = raw_input('What is your favorite subject?')

def mad_lib(string, list_of_variables):
    str_spl = string.split()
    count = 0
    #checking if number of blanks equals to number of variables
    for i in str_spl:
        if "_" in i:
            count += 1
            index = str_spl.index(i)
            str_spl[index] = '%s' 
    if count != len(list_of_variables):
        print 'Error'
        return

    
    






            
    return ' '.join(str_spl) % (name, subject)        
    

print mad_lib("___(name)___'s favorite subject in school is ___(subject)___.", 'josh', 'ballet')
# add prompting a user about filling the blanks no matter how many blanks it has