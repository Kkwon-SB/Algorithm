#https://school.programmers.co.kr/learn/courses/30/lessons/181841
#꼬리 문자열

def solution(str_list, ex):
    answer = ''
    for i in str_list:
        if ex not in i:
            answer += i 
    return answer