#https://school.programmers.co.kr/learn/courses/30/lessons/120829
#각도기

def solution(angle):
    if angle == 180:
        return 4
    if angle > 90:
        return 3
    if angle == 90:
        return 2
    if angle < 90:
        return 1
    
