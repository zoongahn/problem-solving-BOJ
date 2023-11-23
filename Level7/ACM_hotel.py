def cal_room_num(h, n):
    if n % h == 0:
        return h * 100 + n // h
    else:
        return n % h * 100 + n // h + 1


trial = int(input())
for i in range(trial):
    h, w, n = map(int, input().split())
    print(cal_room_num(h, n))
