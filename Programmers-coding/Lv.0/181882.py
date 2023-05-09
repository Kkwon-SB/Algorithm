#https://school.programmers.co.kr/learn/courses/30/lessons/181882
#조건에 맞게 수열 변환하기 1

def solution(arr):
    
    for i in range(len(arr)):
        if arr[i] >= 50 and arr[i] % 2 == 0: #짝
            arr[i] /= 2
            continue
        
        if arr[i] < 50 and arr[i] % 2 == 1: #홀
            arr[i] *= 2
    
    return arr
