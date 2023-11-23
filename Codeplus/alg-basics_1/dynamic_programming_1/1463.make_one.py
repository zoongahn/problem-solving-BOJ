import sys

input = sys.stdin.readline

x = int(input())

# d[i] = i를 1로 만드는데 필요한 최소 연산 횟수
d = [0] * (x + 1)
d[1] = 0
for i in range(2, x + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0 and d[i] > (d[i // 2] + 1):
        d[i] = d[i // 2] + 1
    if i % 3 == 0 and d[i] > (d[i // 3] + 1):
        d[i] = d[i // 3] + 1

print(d[x])
