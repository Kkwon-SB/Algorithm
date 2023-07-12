#https://school.programmers.co.kr/learn/courses/30/lessons/120831
#짝수의 합

def solution(n):
    return sum(i for i in range(2, n+1) if i % 2 == 0)
