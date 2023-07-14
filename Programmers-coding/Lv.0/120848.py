#https://school.programmers.co.kr/learn/courses/30/lessons/120848
#팩토리얼

def solution(n):
    temp = 10
    
    while True:
        if facto(temp) <= n:
            return temp
        else:
            temp -= 1


def facto(num):
    facto = 1
    
    for i in range(1,num+1):
        facto *= i
        
    return facto
