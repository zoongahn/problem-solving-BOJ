import sys

input = sys.stdin.readline

while True:
    n = int(input())
    factors = []

    if n < 0:
        break
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            factors.append(i)
    if n == sum(factors):
        print("{} = ".format(n), end="")
        print(" + ".join(map(str, factors)))
    else:
        print("{} is NOT perfect.".format(n))
