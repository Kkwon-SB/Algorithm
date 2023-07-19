#https://school.programmers.co.kr/learn/courses/30/lessons/120904
#숫자 찾기

def solution(num, k):
    answer = []

    for idx, i in enumerate(str(num)):
        if str(k) == i:
            return idx+1
        
    return -1

#str(num).find(str(k)) + 1


# num = list(str(num))
# return 1+num.index(str(k)) if str(k) in num else -1
