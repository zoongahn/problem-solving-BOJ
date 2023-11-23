import sys

input = sys.stdin.readline

# n = 4
# a = [-1, 5, -100, 4]
n = int(input())
a = list(map(int, input().split()))

d = [a[0]] + [-1001] * (n - 1)
# d[i] = a[i]까지의 연속합의 최댓값

for i in range(1, n):
    if d[i - 1] > 0:
        d[i] = d[i - 1] + a[i]
    else:
        d[i] = a[i]

print(max(d))
