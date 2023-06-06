#https://school.programmers.co.kr/learn/courses/30/lessons/82612
#부족한 금액 계산하기

def solution(price, money, count):
    total = 0
    
    for i in range(1,count+1):
        total += price * i
    
    return 0 if total - money < 0 else total - money 
