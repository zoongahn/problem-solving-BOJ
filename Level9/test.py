def append_star(n):
    if n == 1:
        return ["*"]

    stars = append_star(n // 3)
    l = []

    for star in stars:
        l.append(star * 3)
    for star in stars:
        l.append(star + " " * (n // 3) + star)
    for star in stars:
        l.append(star * 3)
    return l


print("\n".join(append_star(int(input()))))