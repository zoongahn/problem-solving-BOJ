def is_prime_num(number):
    if number == 1:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


trial = int(input())
num_list = list(map(int, input().split()))
count = 0

for number in num_list:
    if is_prime_num(number):
        count += 1

print(count)
