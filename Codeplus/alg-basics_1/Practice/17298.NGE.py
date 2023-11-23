import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
index_stack = []
nge = [-1] * N

# 첫번째 수의 오큰수는 아직 모름
index_stack.append(0)

for i in range(1, N):
    while len(index_stack) > 0 and A[index_stack[-1]] < A[i]:
        nge[index_stack.pop()] = A[i]

    index_stack.append(i)


print(*nge)
