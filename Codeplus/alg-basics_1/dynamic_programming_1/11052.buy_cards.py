import sys

input = sys.stdin.readline

n = int(input())
p = [0] + list(map(int, input().split()))
d = [0, p[1]] + [0] * (n - 1)
# [0, (n*p1), ... ]

for i in range(2, n + 1):
    m = 0
    for j in range(1, i + 1):
        m = max(m, d[i - j] + p[j])
    d[i] = m

print(d[n])
