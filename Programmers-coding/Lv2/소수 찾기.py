def solution(numbers):
    cnt = 0
    for num in range(2, numbers+1):  # 2 부터 입력 '숫자까지' 진행

        for i in range(2, num):
            if num % i == 0:  # 소수가 아님
                break
        else:
            cnt += 1

    return cnt
