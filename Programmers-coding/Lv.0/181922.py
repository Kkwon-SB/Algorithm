#https://school.programmers.co.kr/learn/courses/30/lessons/181922
#수열과 구간 쿼리 4

def solution(arr, queries):
    
    for i in range(len(arr)):
        for query in queries:
            if i == 0 or query[2] == 0:
                if query[0] <= i and query[1] >= i:
                    arr[i] += 1
                    continue
                    
            if query[0] <= i and query[1] >= i and i % query[2] == 0:
                arr[i] += 1
    
    return arr
