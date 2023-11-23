import sys

input = sys.stdin.readline

M, N = map(int, input().split())
MAX = 1000000

is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(N**0.5) + 1):
    # for i in range(2, N // 2):
    # for i in range(2, N):
    if is_prime[i]:
        j = i + i
        while j <= N:
            is_prime[j] = False
            j += i

for i in range(M, N + 1):
    if is_prime[i]:
        print(i)
