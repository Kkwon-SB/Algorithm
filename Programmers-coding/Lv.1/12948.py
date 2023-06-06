#https://school.programmers.co.kr/learn/courses/30/lessons/12948
#핸드폰 번호 가리기

def solution(phone_number):
    temp = len(phone_number)
    return '*' * (temp-4) + phone_number[-4:] 
