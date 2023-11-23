import sys

input = sys.stdin.readline


# 이항(n, k) = n!/(n!(n-k)!)

def factorial(x):
    if x == 1 or x == 0:
        return 1
    return x * factorial(x - 1)


N, K = map(int, input().split())
print(factorial(N) // factorial(K) // factorial(N - K))
