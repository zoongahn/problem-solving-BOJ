def cal_resident_num(k, n):
    num_list = [x+1 for x in range(n)]      # 0층 초기화
    for i in range(k):      # i+1 층
        sum = 0
        for j in range(len(num_list)):      # j+1호
            sum += num_list[j]
            num_list[j] = sum
    return num_list[n-1]


test = int(input())
for i in range(test):
    k = int(input())
    n = int(input())
    print(cal_resident_num(k, n))