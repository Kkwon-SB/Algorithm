#https://school.programmers.co.kr/learn/courses/30/lessons/181893
#배열 조각하기

def solution(arr, query):
    #query 인덱스에 위치한 값이 아닌, 인덱스 값이 기준.
    for i in range(len(query)):
        
        if i % 2 == 0:
            arr = arr[:query[i]+1]
        else:
            arr = arr[query[i]:]

    return arr
