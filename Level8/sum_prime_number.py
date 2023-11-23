def is_prime_num(number):
    if number == 1:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


sum = 0
min_prime = -1
m = int(input())
n = int(input())
for i in range(m, n+1):
    if is_prime_num(i):
        if sum == 0:
            min_prime = i
        sum += i

if min_prime != -1:
    print(sum)
print(min_prime)
