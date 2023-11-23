from collections import Counter
import sys


def get_avg(n, num_list):
    return round(sum(num_list) / n)


def get_med(n, num_list):
    return sorted(num_list)[n // 2]


def get_mode(num_list):
    cnt = Counter(num_list).most_common()
    mode_freq = cnt[0][1]
    mode_list = []
    for t in cnt:
        if t[1] == mode_freq:
            mode_list.append(t[0])
    if len(mode_list) == 1:
        return mode_list[0]
    else:
        return sorted(mode_list)[1]


def get_range(num_list):
    return max(num_list) - min(num_list)


N = int(sys.stdin.readline().rstrip())
l = []
for i in range(N):
    l.append(int(sys.stdin.readline().rstrip()))

print(get_avg(N, l))
print(get_med(N, l))
print(get_mode(l))
print(get_range(l))
