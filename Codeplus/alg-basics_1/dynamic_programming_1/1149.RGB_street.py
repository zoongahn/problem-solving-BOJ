import sys

input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
# n = 3
# a = [[26, 40, 83], [49, 60, 57], [13, 89, 99]]
d = [[0] * 3 for _ in range(n + 1)]
# i번집을 색 j로 칠했을 때, 1~i번 집을 칠하는 비용의 최솟값.

for i in range(1, n + 1):
    d[i][0] = min(d[i - 1][1], d[i - 1][2]) + a[i - 1][0]
    d[i][1] = min(d[i - 1][0], d[i - 1][2]) + a[i - 1][1]
    d[i][2] = min(d[i - 1][0], d[i - 1][1]) + a[i - 1][2]

print(min(d[n]))
