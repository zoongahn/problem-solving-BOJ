import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
# n = 10
# a = [5, 3, 1, 4, 5, 3, 10, 2, 3, 1]

d = [1] * n
# d[i] = a[i]까지의 LIS의 길이. 즉, len(LIS(a[i])).
v = [-1] * n
# v[i] = LIS에서 바로 전 원소의 인덱스 값. 역추적을 위한 포인터 역할

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j] and d[i] < d[j] + 1:
            d[i] = d[j] + 1
            v[i] = j

length_lis = max(d)
index_lis = [i for i, x in enumerate(d) if x == length_lis][0]


# 역추적 함수
def go(p):
    if p == -1:
        return
    go(v[p])
    print(a[p], end=" ")


print(length_lis)
go(index_lis)
print()
