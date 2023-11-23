"""
    merge 과정에서 K번째 저장되는(K번째 merged_list에 들어가는) 값을 구하는 문제이다.
    기존에 구현된 merge sort에 원소가 추가되는 순서를 담을 리스트만 만들면 된다.

    주의할 점은 본 문제에서는 배열을 나눌 때 앞이 크도록(451 32) 나누기 때문에 mid=(len(L)+1)//2 가 된다.
"""
import sys

answer_list = []


def merge(list1, list2):
    global answer_list
    merged_list = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            answer_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            answer_list.append(list1[i])
            i += 1

        if i == len(list1):
            merged_list += list2[j:]
            answer_list += list2[j:]
        elif j == len(list2):
            merged_list += list1[i:]
            answer_list += list1[i:]

    return merged_list


def merge_sort(L):
    if len(L) == 1:
        return L
    mid = (len(L) + 1) // 2

    return merge(merge_sort(L[:mid]), merge_sort(L[mid:]))


input = sys.stdin.readline

N, K = map(int, input().split())
num_list = list(map(int, input().split()))
merge_sort(num_list)
if K < len(answer_list):
    print(answer_list[K - 1])
else:
    print(-1)
