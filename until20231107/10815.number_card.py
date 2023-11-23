import sys


def binary_search(sorted_list, n):
    start_index, end_index = 0, len(sorted_list) - 1
    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        if n == sorted_list[mid_index]:
            return 1
        elif n < sorted_list[mid_index]:
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1
    return 0


input = sys.stdin.readline

N = int(input())
user_num = list(map(int, input().split()))
M = int(input())
match_num = list(map(int, input().split()))
user_num.sort()

for n in match_num:
    print(binary_search(user_num, n), end=" ")
