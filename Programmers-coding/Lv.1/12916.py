#https://school.programmers.co.kr/learn/courses/30/lessons/12916
#문자열 내 p와 y의 개수

#문자열을 전체 대문자 or 소문자로 변경
#count 후 비교

def solution(s):
    s = s.upper()
    p_num = s.count('P')
    y_num = s.count('Y')
    
    return True if p_num == y_num else False
