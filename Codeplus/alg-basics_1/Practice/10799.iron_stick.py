import sys

input = sys.stdin.readline


def get_stick_num(s: str):
    index_stack = []
    result = 0
    for i in range(len(s)):
        char = s[i]
        if char == "(":
            index_stack.append(i)
        elif char == ")":
            if (i - index_stack[-1]) == 1:  # 레이저
                index_stack.pop()
                result += len(index_stack)
            else:
                index_stack.pop()
                result += 1
    return result


print(get_stick_num(input()))
