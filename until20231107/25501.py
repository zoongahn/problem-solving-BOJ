from sys import stdin

count = 0


def recursion(s, l, r):
    global count
    count += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l + 1, r - 1)


def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)


N = int(stdin.readline())
word_list = []
for i in range(N):
    word_list.append(stdin.readline().rstrip())

for word in word_list:
    print(isPalindrome(word), count)
    count = 0
