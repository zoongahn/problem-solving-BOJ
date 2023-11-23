chess = [1, 1, 2, 2, 2, 8]
input_list = list(map(int, input().split()))

print(*list(map(lambda x, y: x - y, chess, input_list)))
