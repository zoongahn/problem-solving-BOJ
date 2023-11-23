import sys

input = sys.stdin.readline

# n = 13
# a = [5, 3, 1, 4, 5, 3, 10, 2, 3, 4, 5, 6, 15]
n = int(input())
a = list(map(int, input().split()))
d = [1] * n
# d[i] = a[i]를 마지막으로 하는 가장긴증가하는부분수열의 길이

for i in range(1, n):
    for j in range(0, i):
        if a[i] > a[j]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))
