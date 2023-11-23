def append_star(n):
    if n == 1:
        return list("*")        # 재귀함수가 1까지 도달 => "*"리턴

    stars = append_star(n // 3)
    l = []

    for star in stars:
        l.append(star * 3)
    for star in stars:
        l.append(star + " " * (n // 3) + star)
    for star in stars:
        l.append(star * 3)

    return l


print('\n'.join(append_star(int(input()))))
# "구분자".join(리스트) : 리스트의 원소사이에 구분자를 삽입하고 하나의 문자열로 합침.
