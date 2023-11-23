# https://ooyoung.tistory.com/111 참조

import sys

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
for i in range(N):
    x1, y1, r1, x2, y2, r2 = arr[i]
    dis = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if (x1, y1, r1) == (x2, y2, r2):  # 두 원의 중심과 반지름이 모두 같을 경우
        print(-1)
    elif abs(r1 - r2) == dis or r1 + r2 == dis:  # 두 원이 내접 or 외접 할 경우
        print(1)
    elif abs(r1 - r2) < dis < r1 + r2:  # 두 원이 서로다른 두 점에서 만날 경우
        print(2)
    else:  # 만나지 않을 경우
        print(0)
