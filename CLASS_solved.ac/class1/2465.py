l = list(map(int, input().split()))
x = 0
for i in range(len(l)):
    x += l[i] ** 2

print(str(x)[-1])
