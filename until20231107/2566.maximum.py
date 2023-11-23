def get_max_value(mylist):
    return max(mylist)


def get_max_index(mylist):
    ret_index = None
    M = -1
    for index in range(len(mylist)):
        if M < mylist[index]:
            M = mylist[index]
            ret_index = index
    return ret_index


def input_int_list():
    return list(map(int, input().split()))


m = -1
r, c = -1, -1
for i in range(9):
    arr = input_int_list()
    x = max(arr)
    if m < x:
        m = x
        r, c = i + 1, get_max_index(arr) + 1

print(m)
print(r, c)
