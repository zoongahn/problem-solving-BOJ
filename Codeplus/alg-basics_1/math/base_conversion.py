def ten_to_n(n, number):
    result = ""
    while number > 0:
        result = str(number % n) + result
        number = number // n
    return result


def n_to_ten(n, number: str):
    result = int(number[-1])
    for i in range(2, len(number) + 1):
        result += int(number[-i]) * (n ** (i - 1))
    return result


print(ten_to_n(3, 11))
print(n_to_ten(3, "102"))
