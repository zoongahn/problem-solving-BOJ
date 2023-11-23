import sys
from math import gcd
from math import sqrt

input = sys.stdin.readline

# X를 M으로 나누었을때의 몫을 x, 나머지를 R이라 하고, 입력값 N = 3이라 가정하자.(단, X1 >= X2 >= X3)
# 이때 M은 나누는 수, 즉 문제에서 구하려는 결과값임에 주목하라.
# X1 = M * x1 + R
# X2 = M * x2 + R
# X3 = M * x3 + R 을 만족한다.

# R을 소거하면,
# X1 - X2 = M * (x1 - x2)
# X2 - X3 = M * (x2 - x3) 인데,
# 이때, M은 어떤 두 자연수 (X1 - X2), (X2 - X3)의 공약수가 된다.
# N이 3이 아닌 다른 정수인 경우에도 마찬가지.


N = int(input())
numbers = [int(input()) for i in range(N)]
numbers.sort()
intervals = []  # [(X1-X2), (X2-X3), ...]
answer = []
for i in range(N - 1):
    intervals.append(numbers[i + 1] - numbers[i])

prev_gcd = intervals[0]
# loop을 돌며 intevals내 모든 수의 최대공약수 탐색.
for i in range(1, len(intervals)):
    prev_gcd = gcd(prev_gcd, intervals[i])

# 공약수 = 최대공약수의 약수
# 이때, 상한을 prev_gcd로 하여 최대공약수까지로 반복문을 돌리면 너무 오래걸림.
# 상한을 최대공약수의 제곱근으로 하고, 두 조건하에서 공약수들을 탐색.
# i)    gcd % i == 0    -> i가 공약수
# ii)   gcd // i == Q(몫)    -> Q 역시 gcd의 약수
for i in range(2, int(sqrt(prev_gcd)) + 1):
    if prev_gcd % i == 0:
        answer.append(i)  # i)
        answer.append(prev_gcd // i)  # ii)
answer.append(prev_gcd)
answer = list(set(answer))  # 중복된 값이 있을수도 -> 중복 제거
answer.sort()  # 정렬
print(*answer)
