#https://school.programmers.co.kr/learn/courses/30/lessons/181930
#주사위 게임 2

def solution(a, b, c):
    answer = 0
    
    if a == b and b == c: #3개 같은 경우
        answer = (a + b + c) * ((a*a) + (b*b) + (c*c)) * ((a*a*a) + (b*b*b) + (c*c*c)) 
    elif a == b or b == c or a== c: #2개 같은 경우
        answer = (a + b + c) * ((a*a) + (b*b) + (c*c)) 
    else: #각자 다른 경우
        answer = a + b + c
    
    return answer
