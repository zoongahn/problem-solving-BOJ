import sys
from collections import Counter

input = sys.stdin.readline


def fashion_case(l: list):
    if len(l) == 0:
        return 0
    tmp = l[0] + 1
    for i in range(1, len(l)):
        tmp *= (l[i] + 1)
    return tmp - 1


T = int(input())
for i in range(T):
    tmp = []
    N = int(input())
    for i in range(N):
        a, b = input().split()
        tmp.append(b)
    fashion_counter = list(Counter(tmp).values())
    print(fashion_case(fashion_counter))
