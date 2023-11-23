import sys

input = sys.stdin.readline

n = int(input())
d = [1] * (n + 1)


for i in range(2, n + 1):
    d[i] = d[i - 1] + d[i - 2]


print(d[n] % 10007)
