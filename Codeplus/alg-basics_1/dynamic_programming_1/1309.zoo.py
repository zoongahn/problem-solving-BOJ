import sys

input = sys.stdin.readline

n = int(input())
MOD = 9901

d = [[1] * 3 for i in range(n + 1)]
# d[i] = [배치X, 왼쪽배치, 오른쪽배치]

for i in range(2, n + 1):
    for j in range(4):
        if j == 0:
            d[i][j] = (sum(d[i - 1])) % MOD
        elif j == 1:
            d[i][j] = (d[i - 1][0] + d[i - 1][2]) % MOD
        elif j == 2:
            d[i][j] = (d[i - 1][0] + d[i - 1][1]) % MOD

print(sum(d[n]) % MOD)
