#https://school.programmers.co.kr/learn/courses/30/lessons/120862
#최댓값 만들기 (2)

def solution(num):
    num.sort()
    
    temp1 = num[0] * num[1]
    temp2 = num[-1] * num[-2]
    
    return temp1 if temp1 > temp2 else temp2

    # return num[0] * num[1] if num[0] * num[1] > num[-1] * num[-2] else num[-1] * num[-2]
