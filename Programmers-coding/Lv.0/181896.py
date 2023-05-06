#https://school.programmers.co.kr/learn/courses/30/lessons/181896
#첫 번째로 나오는 음수

def solution(num_list):
    
    for idx, i in enumerate(num_list):
        if i < 0:
            return idx
    return -1 
