import sys

input = sys.stdin.readline

n = int(input())
a = [[0]] + [list(map(int, input().split())) for i in range(n)]
d = [[0], a[1]]

for i in range(2, n + 1):
    tmp = []
    tmp.append(d[i - 1][0] + a[i][0])
    for j in range(1, i - 1):
        tmp.append(max(d[i - 1][j - 1], d[i - 1][j]) + a[i][j])
    tmp.append(d[i - 1][i - 1 - 1] + a[i][i - 1])
    d.append(tmp)

print(max(d[n]))
