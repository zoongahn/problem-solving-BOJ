n = int(input())
count = 0

if n % 5 == 0:
    count = n // 5
else:
    for i in range(n // 5 + 1):
        tmp = n - (n // 5 - i) * 5
        if tmp % 3 == 0:
            count = (n // 5 - i) + (tmp // 3)
            break

if count == 0:
    print(-1)
else:
    print(count)
