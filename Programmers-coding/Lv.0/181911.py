#https://school.programmers.co.kr/learn/courses/30/lessons/181911
#부분 문자열 이어 붙여 문자열 만들기

def solution(my_strings, parts):
    answer = ''
    
    for word, part in zip(my_strings, parts):
        answer += word[part[0]:part[1]+1]    
    
     
    return answer
