import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    d = [1, 1, 2, 4] + [0] * (n - 3)

    for i in range(4, n + 1):
        d[i] = d[i - 1] + d[i - 2] + d[i - 3]

    print(d[n])
