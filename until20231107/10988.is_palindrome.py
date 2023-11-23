import sys

input = sys.stdin.readline

t = input().strip()
l = len(t)

b = 1

for i in range(l // 2):
    if t[i] != t[l - 1 - i]:
        b = 0
        break

print(b)
