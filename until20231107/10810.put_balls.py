import sys

input = sys.stdin.readline

n, m = map(int, input().split())
l = [0] * n
for i in range(m):
    a, b, c = map(int, input().split())
    for j in range(a - 1, b):
        l[j] = c

print(*l)
