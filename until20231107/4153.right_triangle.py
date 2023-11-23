import sys


def is_right(points: list):
    points.sort()
    if points[0] ** 2 + points[1] ** 2 == points[2] ** 2:
        return "right"
    else:
        return "wrong"


input = sys.stdin.readline

user_list = []
while True:
    p = list(map(int, input().split()))
    if p == [0, 0, 0]:
        break
    user_list.append(p)

for p in user_list:
    print(is_right(p))
