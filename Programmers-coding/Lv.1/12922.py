#https://school.programmers.co.kr/learn/courses/30/lessons/12922
#수박수박수박수박수박수?

def solution(n):
    mok, rest = divmod(n, 2)
    
    return ('수박' * mok) + ('수' * rest)
