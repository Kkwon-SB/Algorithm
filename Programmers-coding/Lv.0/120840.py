#https://school.programmers.co.kr/learn/courses/30/lessons/120840
#구슬을 나누는 경우의 수

def solution(balls, share):
    return factorial(balls) / (factorial(balls-share) * factorial(share))


def factorial(num):
    facto = 1
    
    for i in range(1, num + 1):
        facto *= i
    
    return facto
