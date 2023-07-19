#https://school.programmers.co.kr/learn/courses/30/lessons/120909
#제곱수 판별하기

def solution(n):
    return 1 if n == int(n ** 0.5) * int(n ** 0.5) else 2 

    # return 1 if n ** 0.5 == int(n ** 0.5) else 2
