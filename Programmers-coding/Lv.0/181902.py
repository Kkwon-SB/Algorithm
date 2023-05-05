#https://school.programmers.co.kr/learn/courses/30/lessons/181902
#문자 개수 세기

#대문자 65 ~ 90 ,소문자 97 ~ 122
def solution(my_string):
    answer = []

    for i in range(65,91): #대문자
        answer.append(my_string.count(chr(i)))
    
    for i in range(97,123): #소문자
        answer.append(my_string.count(chr(i)))
    
    return answer
