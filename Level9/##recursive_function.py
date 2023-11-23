def recursive_function(i):
    if i == 10:
        return
    print("{}번째 재귀함수에서 {}번째 재귀함수를 호출합니다.".format(i, i+1))
    recursive_function(i+1)

    print("{}번째 재귀함수를 종료합니다.".format(i))


recursive_function(1)