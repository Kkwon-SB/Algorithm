#https://school.programmers.co.kr/learn/courses/30/lessons/181844
#배열의 원소 삭제하기

def solution(arr, delete_list):

    for i in range(len(arr)-1, -1, -1):
        if arr[i] in delete_list:
            arr.remove(arr[i])
    return arr
    
    
'''
    #인덱스 꼬임
    for i in arr:
        if i in delete_list:
            arr.remove(i)
    return arr
'''
