#https://school.programmers.co.kr/learn/courses/30/lessons/70128
#내적

def solution(a, b):
    total = 0 
    
    for i, j in zip(a, b):
        total += i * j    
        
    return total
