import sys

input = sys.stdin.readline


def print_stack(s: list):
    while len(s) > 0:
        print(s.pop(), end="")


def reverse_word(word):
    char_stack = []
    is_tag = False
    for char in word:
        if char == "<":
            is_tag = True
            print_stack(char_stack)
            print(char, end="")
        elif char == ">":
            is_tag = False
            print(char, end="")
        elif is_tag:
            print(char, end="")
        else:
            if char == " ":
                print_stack(char_stack)
                print(char, end="")
            else:
                char_stack.append(char)

    print_stack(char_stack)
    print()


s = input().strip()
reverse_word(s)
