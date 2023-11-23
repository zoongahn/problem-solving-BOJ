def add_list(list1, list2):
    return list(map(lambda x, y: x + y, list1, list2))


def print_llist(two_dimensional_list):
    for l in two_dimensional_list:
        print(*l)


def get_ints():
    return map(int, input().split())


N, M = get_ints()
A, B = [], []
for i in range(N):
    A.append(list(get_ints()))
for i in range(N):
    B.append(list(get_ints()))

for i in range(N):
    A[i] = add_list(A[i], B[i])

print_llist(A)
