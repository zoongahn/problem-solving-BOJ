arr = [[0 for i in range(100)] for j in range(100)]
count = 0
N = int(input())
for i in range(N):
    h, w = map(int, input().split())
    for j in range(h, h + 10):
        for k in range(w, w + 10):
            if arr[j][k] == 0:
                arr[j][k] = 1
                count += 1

print(count)
