# https://itcrowd2016.tistory.com/84 참조

import sys

input = sys.stdin.readline

N = 6
K = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
width_max, width_max_index = 0, 0  # 가로길이 최댓값 & 해당 인덱스
height_max, height_max_index = 0, 0  # 세로길이 최댓값 & 해당 인덱스
for i in range(N):
    if arr[i][0] == 1 or arr[i][0] == 2:  # 방향이 (동 또는 서)일 경우 -> 가로길이
        if width_max < arr[i][1]:
            width_max = arr[i][1]
            width_max_index = i
    else:  # 방향이 (남 또는 북)일 경우 -> 세로길이
        if height_max < arr[i][1]:
            height_max = arr[i][1]
            height_max_index = i

# 뺄 사각형의 가로는 longgest width의 양 옆 heights의 차의 절댓값임을 이용.
sub_width = abs(arr[(width_max_index - 1) % N][1] - arr[(width_max_index + 1) % N][1])
# 뺄 사각형의 세로는 longgest height의 양 옆 widths의 차의 절댓값임을 이용.
sub_height = abs(arr[(height_max_index - 1) % N][1] - arr[(height_max_index + 1) % N][1])

answer = K * ((width_max * height_max) - (sub_width * sub_height))
print(answer)
