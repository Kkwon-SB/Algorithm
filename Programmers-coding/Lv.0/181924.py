#https://school.programmers.co.kr/learn/courses/30/lessons/181924
#수열과 구간 쿼리 3

def solution(arr, queries):
    # answer = []
    
    for query in queries:
        i, j = query[0], query[1]
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    
    return arr
