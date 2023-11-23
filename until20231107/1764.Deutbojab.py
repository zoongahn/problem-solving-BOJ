import sys

input = sys.stdin.readline
N, M = map(int, input().split())
N_set = set([input().strip() for i in range(N)])
M_set = set([input().strip() for j in range(M)])

result_set = sorted(N_set & M_set)
print(len(result_set))
for word in result_set:
    print(word)
