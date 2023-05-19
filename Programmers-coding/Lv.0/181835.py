#https://school.programmers.co.kr/learn/courses/30/lessons/181835
#조건에 맞게 수열 변환하기 3

def solution(arr, k):

    if k % 2 == 0: #짝
        arr = [i+k for i in arr]
        return arr
    
    
    if k % 2 == 1: #홀
        arr = [i*k for i in arr]
        return arr
