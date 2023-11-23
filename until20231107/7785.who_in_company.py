import sys
import time

start = time.time()

input = sys.stdin.readline

t = int(input())

log = {}
for i in range(t):
    name, action = input().split()
    match action:
        case "enter":
            log[name] = True
        case "leave":
            del log[name]

log = sorted(log, reverse=True)

for n in log:
    print(n)

# print(time.time() - start)
