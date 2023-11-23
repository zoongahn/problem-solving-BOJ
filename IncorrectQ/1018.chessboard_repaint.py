N, M = map(int, input().split())
board = []
result = []
for i in range(N):
    board.append(input())

for i in range(N - 7):
    for j in range(M - 7):
        draw_count1 = 0  # case1: the starting point is "B"
        draw_count2 = 0  # case2: the starting point is "W"
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:
                    if board[x][y] != "B":
                        draw_count1 += 1
                    if board[x][y] != "W":
                        draw_count2 += 1
                else:
                    if board[x][y] != "B":
                        draw_count2 += 1
                    if board[x][y] != "W":
                        draw_count1 += 1
        result.append(draw_count1)
        result.append(draw_count2)

print(min(result))
