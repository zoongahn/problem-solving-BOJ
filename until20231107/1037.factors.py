import sys

input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
N = max(numbers) * min(numbers)
print(N)
