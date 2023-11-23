import sys

input = sys.stdin.readline

mod = 1000000009
limit = 100000
d = [[0], [1, 0, 0], [0, 1, 0], [1, 1, 1]] + [
    [0 for j in range(3)] for i in range(limit - 3)
]
# d[i][j] = i를 1,2,3의 합으로 나타낼때 j+1로 끝나는 방법의 수

for i in range(4, limit + 1):
    d[i][1] = d[i - 2][0] + d[i - 2][2]
    d[i][2] = d[i - 3][0] + d[i - 3][1]
    d[i][0] = d[i - 1][1] + d[i - 1][2]

t = int(input())
for _ in range(t):
    n = int(input())
    print(sum(d[n]) % mod)
