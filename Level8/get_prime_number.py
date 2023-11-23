def is_prime(number):
    if number == 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


m, n = map(int, input().split())

for number in range(m, n + 1):
    if is_prime(number):
        print(number)
