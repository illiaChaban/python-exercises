# ls = [5, 'a', 'b', 3, True, -1, 'b', -1, False, False, 5]
# the_right_answer = [5, 'a', 'b', 3, True, -1, False]
# new_ls = []
# for i in ls:
#   if not i in new_ls:
#     new_ls.append(i)
# print new_ls
# print new_ls == the_right_answer

ls = [5, 'a', 'b', 3, True, -1, 'b', -1, False, False, 5]
the_right_answer = [5, 'a', 'b', 3, True, -1, False]

def dedup(ls1):
    new_ls = []
    for i in ls:
        if not i in new_ls:
            new_ls.append(i)
    return new_ls

print dedup(ls)