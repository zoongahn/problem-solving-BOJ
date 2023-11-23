import sys

input = sys.stdin.readline

max = 1000000


is_prime = [True] * (max + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, max + 1):
    if is_prime[i]:
        j = i + i
        while j <= max:
            is_prime[j] = False
            j += i

while True:
    n = int(input())
    if n == 0:
        break

    for a in range(3, max + 1, 2):
        if is_prime[a] and is_prime[n - a]:
            print("{} = {} + {}".format(n, a, n - a))
            break
