#https://school.programmers.co.kr/learn/courses/30/lessons/120825
#문자 반복 출력하기

def solution(my_string, n):
    # answer = ''
    # for i in my_string:
    #     answer += i * n
    # return answer
    return ''.join(i * n for i in my_string)
