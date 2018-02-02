alpha = 'abcdefghijklmnopqrstuvwxyza  '
string = raw_input('String to Caesar Cipher: ')
new_str = ''
for i in range(0, len(string)):
    # if string[i] == ' ':
    #     new_str += ' '
    # else:
        index_in_alpha = alpha.index(string[i])
        new_str += alpha[index_in_alpha + 1]
print new_str