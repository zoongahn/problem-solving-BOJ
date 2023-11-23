# https://insight-bgh.tistory.com/337 참고
# https://zoong.notion.site/2004-combination_zero_count-a80fa67e0f76423caed172e4ed7c03fc 노션 정리본

import sys

input = sys.stdin.readline


# 어떤 수 n!의 끝자리 k의 갯수를 리턴하는 함수
def digit_counter(n, k):
    count = 0
    while n != 0:
        n = n // k
        count += n
    return count


n, m = map(int, input().split())

answer = min(digit_counter(n, 2) - digit_counter(m, 2) - digit_counter(n - m, 2),
             digit_counter(n, 5) - digit_counter(m, 5) - digit_counter(n - m, 5))
print(answer)
