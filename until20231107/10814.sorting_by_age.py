from sys import stdin


def inp():
    return stdin.readline().rstrip()


def read_member():
    member = list(inp().split())
    member[0] = int(member[0])
    return tuple(member)


N = int(inp())
coor_list = []
for i in range(N):
    coor_list.append(read_member())
coor_list.sort(key=lambda x: (x[0]))

for t in coor_list:
    print(*t)
