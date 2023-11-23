import sys

input = sys.stdin.readline

N, M = map(int, input().split())
pok_dict = {}
for i in range(1, N + 1):
    pok = input().strip()
    index = str(i)
    pok_dict[index] = pok
    pok_dict[pok] = index

for j in range(M):
    quest = input().strip()
    print(pok_dict[quest])
