# 정답은 맞췄지만 Test Case 8,10 ,12번 런타임or 시간초과로 실패
def solution(number, k):
    number = list(number)
    k_num = 0
    i = 0  # for문이 아닌 while문으로 실행, 비교할 index자리를 위한 i

    while k_num != k:  # 제거할 수 있는 수가 다 채워지면 STOP
        if number[i] >= number[i + 1]:
            i += 1
        else:
            number = number[:i] + number[i + 1 :]  # number.remove(number[i])의 대체 코드
            k_num += 1
            i = 0
    Str_number = "".join(number)

    return Str_number
