#https://school.programmers.co.kr/learn/courses/30/lessons/181861
#배열의 원소만큼 추가하기

def solution(arr):
    answer = []
    
    for i in arr:
        answer+= [i] * i
        
    return answer
