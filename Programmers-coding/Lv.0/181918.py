#https://school.programmers.co.kr/learn/courses/30/lessons/181918
#배열 만들기 4

def solution(arr):
    i = 0
    stk = []
    
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        
        if stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        else:
            del stk[-1]
    
    
    return stk
