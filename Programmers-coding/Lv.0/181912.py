#https://school.programmers.co.kr/learn/courses/30/lessons/181912
#배열 만들기 5

def solution(intStrs, k, s, l):
    answer = []
    
    for arr in intStrs:
        target = int(arr[s:s+l])
        if k < target:
            answer.append(target)
    
    return answer
