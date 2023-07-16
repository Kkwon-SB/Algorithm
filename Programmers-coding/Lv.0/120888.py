#https://school.programmers.co.kr/learn/courses/30/lessons/120888
#중복된 문자 제거

def solution(my_string):
    answer = ''

    for i in my_string:
        if i not in answer:
            answer += i
    
    return answer

'''
dict.fromkeys(my_string) // 인자로 2개 (Key, value) 가능, value 없을 경우 None 처리 
키 중심이라 중복 제거

'''
