#https://school.programmers.co.kr/learn/courses/30/lessons/181915
#글자 이어 붙여 문자열 만들기

def solution(my_string, index_list):
    answer = ''
    
    for i in index_list:
        answer += my_string[i]
    return answer
