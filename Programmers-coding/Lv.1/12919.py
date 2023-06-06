#https://school.programmers.co.kr/learn/courses/30/lessons/12919
#서울에서 김서방 찾기

def solution(seoul):
    for idx, elm in enumerate(seoul):
        if elm == 'Kim':
            return '김서방은 ' + str(idx) + '에 있다'
 
