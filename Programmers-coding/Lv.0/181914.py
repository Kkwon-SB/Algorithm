#https://school.programmers.co.kr/learn/courses/30/lessons/181914
#9로 나눈 나머지

def solution(number):
    sum = 0
    for i in list(number):
        sum += int(i)
    
    return sum % 9
