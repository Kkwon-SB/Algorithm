#https://school.programmers.co.kr/learn/courses/30/lessons/181831
#특별한 이차원 배열 2

def solution(arr):
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                return 0
    
    return 1
