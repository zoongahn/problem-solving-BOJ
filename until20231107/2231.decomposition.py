import sys

input = sys.stdin.readline

N = int(input())

result = 0
for i in range(N):
    tmp = i + sum(map(int, str(i)))
    if tmp == N:
        result = i
        break

print(result)
