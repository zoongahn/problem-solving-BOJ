import sys
from math import factorial

input = sys.stdin.readline


def bi_co(a, b):
    return factorial(a) // factorial(b) // factorial(a - b)


N, K = map(int, input().split())
print(bi_co(N, K) % 10007)
