#https://school.programmers.co.kr/learn/courses/30/lessons/12912
#두 정수 사이의 합

def solution(a, b):
    small = min(a,b)
    big = max(a,b)
         
    return sum(range(small, big + 1))

'''
    total = 0

    for i in range(small, big+1):
        total += i
        
    return total
'''
