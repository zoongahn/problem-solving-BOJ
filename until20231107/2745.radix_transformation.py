import sys

input = sys.stdin.readline

number, radix_ = input().strip().split()
radix = int(radix_)
result = 0

for i in range(len(number)):
    if number[i].isalpha():
        result += (ord(number[i]) - 55) * pow(radix, len(number) - i - 1)
    else:
        result += int(number[i]) * pow(radix, len(number) - i - 1)

print(result)

# 모범답안
# print(int(number, int(radix_)))
