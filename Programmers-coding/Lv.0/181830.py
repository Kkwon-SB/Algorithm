#https://school.programmers.co.kr/learn/courses/30/lessons/181830
#정사각형으로 만들기

def solution(arr):
    
    if len(arr) == len(arr[0]):
        return arr
    
    if len(arr) > len(arr[0]):
        std = len(arr) - len(arr[0])
        for i in range(len(arr)):
            arr[i] += [0] * std
        return arr
    
    if len(arr) < len(arr[0]):
        for _ in range(len(arr[0]) - len(arr)):
            arr.append([0] * len(arr[0]))
        
        
    return arr
