import sys

MAX = 10000
input = sys.stdin.readline
N = int(input())
num_array = [0]*MAX

for i in range(N):
    num_array[int(input()) - 1] += 1

for i in range(MAX):
    if num_array[i] != 0:
        for j in range(num_array[i]):
            print(i + 1)
