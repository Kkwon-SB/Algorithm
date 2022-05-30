#정답은 맞췄지만 Test Case 8,10 ,12번 런타임or 시간초과로 실패
def solution(number, k):
    number = list(number)
    k_num = 0
    i = 0

    while k_num != k:
        if number[i] >= number[i+1]:
            i += 1
        else :
            # number.remove(number[i])
            number=number[:i]+number[i+1:]
            k_num += 1
            i = 0
    Str_number = "".join(number)
    
    return Str_number

