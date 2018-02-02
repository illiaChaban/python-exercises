# string = raw_input('string to leetspeak: ').upper()
# leetspeak = 'AEGIOST'
# leetspeak2 = '4361057'
# new_p = ''
# for i in range(0, len(string)):
#   if string[i] in leetspeak:
#     index_inLS = leetspeak.index(string[i])
#     new_p += leetspeak2[index_inLS]
#   else:
#     new_p += string[i]
# print new_p

string = raw_input('string to leetspeak: ').upper()
def leetspeak(strg):
    leetspeak = {'A': 4, 'E': 3, 'G': 6, 'I': 1, 'O': 0, 'S': 5, 'T': 7}
    new_p = ''
    for i in range(len(strg)):
        if strg[i] in leetspeak:
            new_p += str(leetspeak[strg[i]])
        else:
            new_p += string[i]
    return new_p

print leetspeak(string)