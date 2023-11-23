def get_medium(num_list):
    return sorted(num_list)[len(num_list) // 2]


def get_average(num_list):
    return sum(num_list)//len(num_list)


N = 5
num_list = [int(input()) for i in range(N)]
print(get_average(num_list))
print(get_medium(num_list))
