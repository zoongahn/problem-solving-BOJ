number = input()
l = list(map(int, number))
print("".join(map(str, sorted(l, reverse=True))))
