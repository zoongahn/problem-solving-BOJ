import sys

input = sys.stdin.readline

n = int(input())
d = [0] * (n + 1)
# d[i] = i를 i이하의 제곱수의 합으로 표현할때 항의 최소 개수

for i in range(1, n + 1):
    # 항상 d[i] <= i 이므로 d[i]의 최댓값인 i를 d[i]의 초깃값으로 설정
    d[i] = i
    j = 1
    # 1 <= j*j <= n
    while j * j <= i:
        if d[i] > d[i - j * j] + 1:
            d[i] = d[i - j * j] + 1
        j += 1

print(d[n])
