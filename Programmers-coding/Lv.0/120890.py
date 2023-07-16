#https://school.programmers.co.kr/learn/courses/30/lessons/120890
#가까운 수

def solution(array, n):
    answer = array[0]
    array.sort()
    distance = abs(n-array[0])
    
    for i in range(0, len(array)):
        if distance > abs(n-array[i]):
            distance = abs(n-array[i])
            answer = array[i]
    
    return answer
