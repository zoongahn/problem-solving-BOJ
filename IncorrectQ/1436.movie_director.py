N = int(input())
any_num = 666
count = 0
while True:
    if "666" in str(any_num):
        count += 1
    if count == N:
        break
    any_num += 1

print(any_num)
