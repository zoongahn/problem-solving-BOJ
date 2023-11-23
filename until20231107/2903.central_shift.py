import sys

input = sys.stdin.readline

n = int(input())
length = 2

for i in range(n):
    length += (length - 1)

print(length ** 2)

# 모범답안
# print((1 + 2 ** n) ** 2)
