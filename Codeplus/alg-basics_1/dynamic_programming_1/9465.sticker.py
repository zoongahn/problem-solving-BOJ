import sys

input = sys.stdin.readline

t = int(input())
for z in range(t):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(2)]
    d = [[0, 0, 0] for _ in range(n + 1)]
    # d[i] = [안때는 경우, 위쪽, 아래쪽 스티커를 때는 경우의 점수의 최댓값]

    for i in range(1, n + 1):
        d[i][0] = max(d[i - 1])
        d[i][1] = max(d[i - 1][0], d[i - 1][2]) + a[0][i - 1]
        d[i][2] = max(d[i - 1][0], d[i - 1][1]) + a[1][i - 1]

    print(max(d[n]))
