print '''Please fill in the blanks below:
___(name)___'s favorite subject in school is ___(subject)___.'''
name = raw_input('What is your name?')
subject = raw_input('What is your favorite subject?')
print "%s's favorite subject in school is %s" % (name, subject)