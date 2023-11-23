import sys

input = sys.stdin.readline

T = int(input())
for i in range(T):
    # 출발점
    x1, y1, x2, y2 = map(int, input().split())
    # 행성계의 개수
    n = int(input())
    count = 0  # 행성 간 진입/이탈 횟수

    for j in range(n):  # n개의 행 loop
        cx, cy, cr = map(int, input().split())
        dis1 = (x1 - cx) ** 2 + (y1 - cy) ** 2  # (x1, y1) ~ (j번째 행성의 중심좌표) 거리
        dis2 = (x2 - cx) ** 2 + (y2 - cy) ** 2  # (x2, y2) ~ (j번째 행성의 중심좌표) 거리
        cr_pow = cr ** 2

        # 두 거리 모두 j번째 행성의 반지름보다 작은 경우. -> 두 점 모두 j번째 행성 내부에 있음.
        if cr_pow > dis1 and cr_pow > dis2:
            pass
        # 두 거리 중 하나만 j번째 행성의 반지름보다 작은 경우. -> 하나는 내부에, 다른 하나는 외부에 존재.
        elif cr_pow > dis1 or cr_pow > dis2:
            count += 1

    print(count)
