import sys


def str_binary(str_list, s):
    start, end = 0, len(str_list) - 1
    while start <= end:
        med = (start + end) // 2
        if s == str_list[med]:
            return 1
        elif s < str_list[med]:
            end = med - 1
        else:
            start = med + 1
    return 0


input = sys.stdin.readline
N, M = map(int, input().split())
N_list = [input() for i in range(N)]
M_list = [input() for j in range(M)]
N_list.sort()
count = 0
for word in M_list:
    count += str_binary(N_list, word)
print(count)
