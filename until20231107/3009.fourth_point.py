import sys
from collections import Counter

input = sys.stdin.readline
x = []
y = []
for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x = Counter(x).most_common()
y = Counter(y).most_common()

print(x[1][0], y[1][0])
