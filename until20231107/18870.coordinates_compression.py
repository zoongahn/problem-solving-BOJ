"""
리스트 안에서 자기보다 작은 숫자의 갯수를 세는 문제이다.
즉, 오름차순으로 정렬된 리스트안에서 각 숫자가 가지는 인덱스를 출력하면 된다.
"""
import sys


def inp():
    return sys.stdin.readline().rstrip()


N = int(inp())
user_list = list(map(int, inp().split()))
set_list = list(sorted(set(user_list)))
dic = {set_list[i]: i for i in range(len(set_list))}
for num in user_list:
    print(dic[num], end=" ")
