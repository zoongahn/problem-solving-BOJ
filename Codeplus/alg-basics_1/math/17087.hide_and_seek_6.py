import sys

input = sys.stdin.readline


def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a % b)


def final_gcd(l):
    result = l[0]
    if len(l) == 1:
        return result
    for i in range(1, len(l)):
        result = get_gcd(result, l[i])
    return result


n, s = map(int, input().split())
a = map(int, input().split())
d = list(set(map(lambda x: abs(x - s), a)))

print(final_gcd(d))
