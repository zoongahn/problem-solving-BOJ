def get_cutline(k, score_list):
    score_list.sort(reverse=True)
    return score_list[k - 1]


N, k = map(int, input().split())
x = list(map(int, input().split()))

print(get_cutline(k, x))
