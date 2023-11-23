import sys

N = int(input())
num_list = list(int(sys.stdin.readline()) for i in range(N))
num_list.sort()
for i in num_list:
    print(i)