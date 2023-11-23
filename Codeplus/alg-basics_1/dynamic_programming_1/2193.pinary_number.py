import sys

input = sys.stdin.readline

n = 10
d = [[0, 1]] + [[0, 0] for _ in range(n - 1)]
# d[i][j] = j로 끝나는 i+1자리 이친수의 개수

for i in range(1, n):
    d[i][0] = d[i - 1][0] + d[i - 1][1]
    d[i][1] = d[i - 1][0]

print(sum(d[n - 1]))
