import sys

input = sys.stdin.readline

n = int(input())

for star in range(1, n + 1):
    t = " " * (n - star) + "*" * (2 * star - 1)
    print(t)

for star in range(n - 1, 0, -1):
    t = " " * (n - star) + "*" * (2 * star - 1)
    print(t)
