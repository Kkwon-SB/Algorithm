#https://school.programmers.co.kr/learn/courses/30/lessons/181862
#세 개의 구분자

def solution(myStr):
    answer = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split()
    return answer if len(answer) != 0 else ["EMPTY"]
