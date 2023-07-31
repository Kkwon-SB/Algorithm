#https://school.programmers.co.kr/learn/courses/30/lessons/181923
#수열과 구간 쿼리 2

def solution(arr, queries):
    array = []
    for query in queries:
        arr2 = arr[query[0]:query[1]+1]
        
        std = int(1e9)
        for i in arr2:
            if i > query[2] and std > i:
                std = i
        
        array.append( std if std != int(1e9) else -1 )
        # if std < int(1e9): #바뀜
        #     array.append(std)
        # else:
        #     array.append(-1)


            
    return array
    
