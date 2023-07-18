#https://school.programmers.co.kr/learn/courses/30/lessons/120893
#대문자와 소문자

def solution(my_string):
    answer = ''
    
    for i in my_string:
        if i.islower():
            answer += i.upper()
        else:
            answer += i.lower()
    
    return answer

    # return ''.join([i.upper() if i.islower() else i.lower() for i in my_string])
