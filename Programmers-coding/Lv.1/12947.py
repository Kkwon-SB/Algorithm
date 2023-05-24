#https://school.programmers.co.kr/learn/courses/30/lessons/12947
#하샤드 수

def solution(x):
    std = sum([int(i) for i in str(x)]) 
    return True if x % std == 0 else False
