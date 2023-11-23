from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
ngf = [-1] * N
index_stack = []
freq = Counter(A)

index_stack.append(0)

for i in range(1, N):
    while len(index_stack) > 0 and freq[A[index_stack[-1]]] < freq[A[i]]:
        ngf[index_stack.pop()] = A[i]

    index_stack.append(i)
print(*ngf)
