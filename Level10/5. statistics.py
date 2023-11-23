import sys

def inp():
    return int(sys.stdin.readline())


N = inp()
MAX = 8001
num_array = [0] * MAX


for i in range(N):
    num_array[inp() + 4000] += 1
