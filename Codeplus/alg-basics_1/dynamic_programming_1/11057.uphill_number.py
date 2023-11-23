import sys

input = sys.stdin.readline

n = int(input())
MOD = 10007
d = [[1] * 10 for _ in range(n + 1)]

for i in range(2, n + 1):
    for j in range(0, 10):
        d[i][j] = sum(d[i - 1][: j + 1]) % MOD

print(sum(d[n]) % MOD)
