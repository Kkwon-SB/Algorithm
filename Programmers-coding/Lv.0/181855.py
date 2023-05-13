#https://school.programmers.co.kr/learn/courses/30/lessons/181855
#문자열 묶기

def solution(strArr):
    len_arr = [0] * 31
    
    for i in strArr:
        len_arr[len(i)] += 1
        
    return max(len_arr)
