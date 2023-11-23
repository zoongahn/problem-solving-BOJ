import sys
from collections import Counter

input = sys.stdin.readline


def search(my_list, n):
    start, end = 0, len(my_list) - 1
    while start <= end:
        med = (start + end) // 2
        if n == my_list[med][0]:
            return my_list[med][1]
        elif n < my_list[med][0]:
            end = med - 1
        else:
            start = med + 1
    return 0


N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))
Counter_N_list = sorted(Counter(N_list).most_common())
for quest in M_list:
    print(search(Counter_N_list, quest), end=" ")
