import sys

input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]
d = [[0, 0, 0] for __ in range(n + 1)]
# d[i] = [안마시는, 1번연속, 2번연속으로 마시는 경우의 최댓값]

for i in range(1, n + 1):
    d[i][0] = max(d[i - 1])
    d[i][1] = d[i - 1][0] + a[i - 1]
    d[i][2] = d[i - 1][1] + a[i - 1]

print(max(d[n]))
