#https://school.programmers.co.kr/learn/courses/30/lessons/181856
#배열 비교하기

def solution(arr1, arr2):

    if len(arr1) != len(arr2):
        if len(arr1) > len(arr2):
            return 1
        else:
            return -1
    
    if sum(arr1) == sum(arr2):
        return 0
    
    if sum(arr1) > sum(arr2):
        return 1
    else:
        return -1
