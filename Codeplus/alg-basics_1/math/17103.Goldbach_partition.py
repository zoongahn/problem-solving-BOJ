import sys

input = sys.stdin.readline

MAX = 1000000


def get_is_prime():
    is_prime = [False, False] + [True] * (MAX - 1)
    for i in range(2, MAX + 1):
        if is_prime[i]:
            j = i + i
            while j <= MAX:
                is_prime[j] = False
                j += i

    return is_prime


def count_partition(number):
    count = 0
    if number == 4:
        return 1
    for i in range(3, number // 2 + 1, 2):
        if is_prime[i] and is_prime[number - i]:
            count += 1
    return count


is_prime = get_is_prime()

# T = int(input())
# for i in range(T):
print(count_partition(int(input())))
