size = int(input())
numbers = []

for i in range(size):
    numbers.append(int(input()))

l=len(numbers)
for i in range(l):
    for j in range(i + 1, l):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

for n in numbers:
    print(n)