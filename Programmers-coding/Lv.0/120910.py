#https://school.programmers.co.kr/learn/courses/30/lessons/120910
#세균 증식

def solution(n, t):
    
    for _ in range(t):
        n *= 2
    
    return n

    # return n*(2**t)
