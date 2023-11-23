def fibonacci(n):
    a, b = 0, 1
    if n == a or n == b:
        return n
    for i in range(n-1):
        a, b = b, a + b
    return b


print(fibonacci(int(input())))