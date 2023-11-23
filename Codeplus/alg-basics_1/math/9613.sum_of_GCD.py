from __future__ import annotations
import sys

input = sys.stdin.readline


def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a % b)


def sum_of_gcd(l: list[int]):
    result = []
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            result.append(get_gcd(l[i], l[j]))
    return sum(result)


t = int(input())
for _ in range(t):
    print(sum_of_gcd(list(map(int, input().split()))[1:]))
