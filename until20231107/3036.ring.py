import sys

input = sys.stdin.readline


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


N = int(input())
num_list = list(map(int, input().split()))
cret = num_list[0]
for i in range(1, N):
    g = gcd(cret, num_list[i])
    print("{}/{}".format(cret // g, num_list[i] // g))
