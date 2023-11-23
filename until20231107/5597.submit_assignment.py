import sys

input = sys.stdin.readline

n = 30
l = [False] * n

for i in range(n - 2):
    l[int(input()) - 1] = True

for i in range(len(l)):
    if l[i] is False:
        print(i + 1)
