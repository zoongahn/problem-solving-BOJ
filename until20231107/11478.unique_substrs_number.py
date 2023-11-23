import sys

input = sys.stdin.readline

my_str = input().rstrip()
substrs = set()

for i in range(len(my_str)):
    for j in range(i, len(my_str)):
        substrs.add(my_str[i:j + 1])

print(len(substrs))
