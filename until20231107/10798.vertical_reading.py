import sys

input = sys.stdin.readline

line = 5
MAX = 15 * 5
result = [""] * MAX

for i in range(line):
    t = input().strip()
    for j in range(len(t)):
        result[i + j * 5] = t[j]

print("".join(result))
