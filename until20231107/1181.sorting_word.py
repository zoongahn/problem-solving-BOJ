from sys import stdin


def inp():
    return stdin.readline().rstrip()


word_list = []
N = int(inp())
for i in range(N):
    w = inp()
    if w not in word_list:
        word_list.append(w)

word_list.sort(key=lambda x: (len(x), x))

for word in word_list:
    print(word)
