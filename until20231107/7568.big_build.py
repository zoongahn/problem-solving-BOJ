import sys

input = sys.stdin.readline

N = int(input())
l = [list(map(int, input().split())) for i in range(N)]
size_list = [1] * N

for i in range(N):
    for j in range(i, N):
        if l[i][0] > l[j][0] and l[i][1] > l[j][1]:
            size_list[j] += 1
        elif l[i][0] < l[j][0] and l[i][1] < l[j][1]:
            size_list[i] += 1

for size in size_list:
    print(size, end=" ")
