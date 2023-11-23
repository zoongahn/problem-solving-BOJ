from sys import stdin


def inp():
    return stdin.readline().rstrip()


N = int(inp())
coor_list = []
for i in range(N):
    coor_list.append(tuple(map(int, inp().split())))
coor_list.sort(key=lambda x: (x[0], x[1]))

for t in coor_list:
    print(*t)
