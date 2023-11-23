import sys

input = sys.stdin.readline

# n = int(input())
n = int(input())
DIGIT = 10
MOD = 1000000000
d = [[0] + [1] * (DIGIT - 1)] + [[0] * DIGIT for _ in range(n - 1)]
# d[i][j] = 길이가 (i+1)이면서 숫자j로 끝나는 계단 수

for i in range(2, n + 1):
    d[i - 1][0] = d[i - 2][1]
    for j in range(1, DIGIT - 1):
        d[i - 1][j] = d[i - 2][j - 1] + d[i - 2][j + 1]
    d[i - 1][9] = d[i - 2][8]


print(sum(d[n - 1]) % MOD)
