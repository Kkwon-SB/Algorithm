#https://school.programmers.co.kr/learn/courses/30/lessons/181895
#배열 만들기 3

def solution(arr, intervals):
    answer = []
    
    for i, j in intervals:
        answer += arr[i:j+1]
    
    return answer
