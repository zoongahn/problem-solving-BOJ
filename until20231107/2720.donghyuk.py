import sys

input = sys.stdin.readline

t = int(input())
cret = [25, 10, 5, 1]

for i in range(t):
    change = []
    n = int(input())
    for j in cret:
        change.append(n // j)
        n %= j
    print(*change)
