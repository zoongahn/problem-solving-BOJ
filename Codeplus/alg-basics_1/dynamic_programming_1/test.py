import sys

input = sys.stdin.readline

n = 3
a = [[26, 40, 83], [49, 60, 57], [13, 89, 99]]

previous_idx = -1
total = 0
for i in range(n):
    min_val = 1000
    for j in range(3):
        if previous_idx != j and a[i][j] < min_val:
            min_val = a[i][j]
            previous_idx = j
    total += min_val

print(total)
