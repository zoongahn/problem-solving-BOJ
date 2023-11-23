import sys

input = sys.stdin.readline

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())
b = 1

for n in range(n0, 100 + 1):
    if not a1 * n + a0 <= c * n:
        b = 0
print(b)
