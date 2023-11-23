import math


def is_prime(number):
    if number == 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


MAX = 123456
all_num = list(range(2, MAX * 2 + 1))
prime_num = list(number for number in all_num if is_prime(number))

while True:
    user_num = int(input())
    if user_num == 0:
        break

    print(sum(user_num < i <= user_num * 2 for i in prime_num))
