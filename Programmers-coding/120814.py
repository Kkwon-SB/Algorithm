#https://school.programmers.co.kr/learn/courses/30/lessons/120814
#피자 나눠 먹기 (1)

def solution(n):
    mok, rest = divmod(n , 7)
    return mok + (1 if rest > 0 else 0) 
