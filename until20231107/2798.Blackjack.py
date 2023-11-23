import sys


def inp():
    return sys.stdin.readline()


N, M = map(int, inp().split())

user_list = list(map(int, inp().split()))

m = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            n = user_list[i] + user_list[j] + user_list[k]
            if n <= M:
                m = max(m, n)

print(m)
