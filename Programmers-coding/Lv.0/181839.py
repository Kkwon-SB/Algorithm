#https://school.programmers.co.kr/learn/courses/30/lessons/181839
#주사위 게임 1

def solution(a, b):
    _a = a % 2
    _b = b % 2
    
    if _a == 1 and _b == 1: #모두 홀
        return (a*a) + (b*b)
    if _a == 0 and _b == 0: #모두 홀x (짝)
        return abs(a-b)
    
    return 2 * (a + b) # 홀,짝
