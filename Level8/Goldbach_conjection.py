import math


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


all_primes = list(number for number in range(2, 10000) if is_prime(number))
test = int(input())
for i in range(test):
    answer = {}
    user_num = int(input())
    primes = list(filter(lambda prime: user_num // 2 <= prime < user_num, all_primes))

    for a in primes:
        b = user_num - a
        if is_prime(b):
            print(b, a)
            break
