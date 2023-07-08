#https://school.programmers.co.kr/learn/courses/30/lessons/
#최빈값 구하기

def solution(array):
    
    if len(array) == 1: 
        return array[0]
    
    array.sort()
    max_value = array[0]
    check = False
    max_cnt, cnt = 1 ,  1
    
    for i in range(1, len(array)):
        if array[i-1] == array[i]:
            cnt += 1
            
            if cnt > max_cnt:    
                max_cnt = cnt
                max_value = array[i]
                check = True
            elif cnt == max_cnt:
                check = False

        else:
            cnt = 1
        
    return max_value if check == True else -1


'''
from collections import Counter

def solution(array):
    
    if len(array) == 1: #1개 경우
        return array[0]
    
    cnt = Counter(array)
    answer = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
    
    return answer[0][0] if answer[0][1] != answer[1][1] else -1 #최빈값이 1개 인지 확인 
'''
