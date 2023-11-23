import sys

input = sys.stdin.readline

ans = []

x, y = map(int, input().split())
for i in range(1, x // 2 + 1):
    if x % i == 0:
        ans.append(i)
ans.append(x)

print(ans[y - 1] if len(ans) >= y else 0)
