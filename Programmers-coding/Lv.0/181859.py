#https://school.programmers.co.kr/learn/courses/30/lessons/181859
#배열 만들기 6

def solution(arr):
    stk = []
    i = 0
    
    while i < len(arr):
        if not stk:
            stk.append(arr[i])
            i += 1
        elif stk:
            if stk[-1] == arr[i]:
                del stk[-1]
                i += 1
            elif stk[-1] != arr[i]:
                stk.append(arr[i])
                i += 1
    
    return stk if stk else [-1]
