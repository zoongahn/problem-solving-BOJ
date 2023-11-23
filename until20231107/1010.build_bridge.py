import sys
from math import factorial

input = sys.stdin.readline


# sol1) Dynamic Programming
def bridge_dp(n, m):
    # n*m 배열.
    # dp[i][j] = n=i, m=j 일 때 다리를 놓을 수 있는 경우의 수.
    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

    # n=1 일 때, 경우의 수는 m.
    for j in range(1, m + 1):
        dp[1][j] = j

    # n=i, m=j 일 때의 경우의 수, dp[i][j] = dp[i-1][j-1] + dp[i-1][j-2] + ... + dp[i-1][i-1]
    for i in range(1, n + 1):
        for j in range(i, m + 1):
            for k in range(j - 1, i - 2, -1):
                dp[i][j] += dp[i - 1][k]
    return dp[n][m]


# 조합이란 n개의 원소를 갖는 집합에서 r개의 원소를 선택하는 것으로 정의되며,
# 어떤 순서로 원소를 선택했는지는 중요하지 않기에 순열(permutation)과는 다른 개념이다.
# 순열(permutation)은 n개의 원소를 갖는 집합에서 r개의 원소를 선택하는 것 혹은 그 결과이지만 선택의 순서가 중요하다.
# 같은 원소들을 선택했더라도 선택의 순서가 다르다면 다른 순열이지만,
# 조합은 어떤 순서로 선택을 하던 같은 원소들만 선택했다면 같은 조합이다.

# 다리끼리 서로 겹쳐질 수 없으므로 선택의 순서는 고려하지 않는다(=조합).
# 즉, n개의 다리에서 m개의 다리를 놓는 경우의 수는 mCn = 이항(m, n)과 같다.(m<=n)


# sol2) Combination(조합)
def bridge_com(n, m):
    return factorial(m) // factorial(n) // factorial(m - n)


T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    print(bridge_dp(n, m))
