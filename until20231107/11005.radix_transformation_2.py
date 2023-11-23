import sys

input = sys.stdin.readline

number, radix = map(int, input().split())
result = ""

while number != 0:
    rem = number % radix
    if rem >= 10:
        result = chr(rem + 55) + result
    else:
        result = str(rem) + result
    number = (number - rem) // radix

print("".join(result))
