def push(l: list, x: int):
    l.append(x)


def pop(l: list):
    if len(l) == 0:
        return -1
    return l.pop()


def size(l: list):
    return len(l)


def empty(l):
    return int(len(l) == 0)


def top(l):
    return l[-1]


l = []
N = int(input())
for i in range(N):
    s = input().split()
    cmd = s[0]
    if cmd == "push":
        push(l, int(s[1]))
    elif cmd == "pop":
        print(pop(l))
    elif cmd == "top":
        print(top(l))
    elif cmd == "size":
        print(size(l))
    elif cmd == "empty":
        print(empty(l))
