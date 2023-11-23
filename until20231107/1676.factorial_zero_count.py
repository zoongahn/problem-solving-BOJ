import sys

input = sys.stdin.readline


# n!에서 끝자리 k의 갯수 = n/(k^1) + n/(k^2) + n/(k^3) + ...


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


n = int(input())

count = 0
s = str(factorial(n))
for i in range(len(s) - 1, -1, -1):
    if s[i] == '0':
        count += 1
    else:
        break
print(count)
