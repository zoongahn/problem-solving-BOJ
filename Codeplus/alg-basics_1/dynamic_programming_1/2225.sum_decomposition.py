import sys

input = sys.stdin.readline

n, k = map(int, input().split())
d = [[0] * (k + 1) for _ in range(n + 1)]
# d[i][j] = 0부터 i까지의 정수 j개를 더해서 그 합이 i가 되는 경우의 수
# 0 <= i <= n, 1 <= j <= k
# 합분해의 마지막 수를 l이라 하면, 0 <= l <= i이고,
# 구하려는 d[n][k]는 가능한 모든 d[i-l][j-1]의 합.

d[0][0] = 1
for i in range(0, n + 1):
    for j in range(1, k + 1):
        for l in range(0, i + 1):
            d[i][j] += d[i - l][j - 1]
        d[i][j] %= 1000000000

print(d[n][k])
