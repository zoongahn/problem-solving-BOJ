import sys

input = sys.stdin.readline


# 유클리드 호제법: 두 자연수 a, b에 대하여 a를 b로 나눈 나머지 r에 대해 a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
# 즉, gcd(a, b) = gcd(b, a%b)
# 재귀함수로 구현
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# 반복문으로 구현
def gcd_loop(a, b):
    while b > 0:
        a, b = b, a % b
    return a


# (a * b) = (a, b의 최소공배수) * (a, b의 최대공약수) 임을 이용하여,
# 최소공배수 lcm = x * y = (a * b) / gcd
def lcm(a, b):
    return a * b // gcd(a, b)


x, y = list(map(int, input().split()))
print(gcd(x, y))
print(lcm(x, y))
