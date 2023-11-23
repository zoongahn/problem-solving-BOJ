import sys

input = sys.stdin.readline


def reverse(mylist: list, start, end):
    while start < end:
        mylist[start], mylist[end] = mylist[end], mylist[start]
        start += 1
        end -= 1
    return mylist


n, m = map(int, input().split())

l = list(range(1, n + 1))
for i in range(m):
    a, b = map(int, input().split())
    l = reverse(l, a - 1, b - 1)

print(*l)
