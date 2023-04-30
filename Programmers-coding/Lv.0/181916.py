#https://school.programmers.co.kr/learn/courses/30/lessons/181916
#주사위 게임 3

from collections import Counter

def solution(a, b, c, d):
    arr = sorted(Counter([a, b, c, d]).items(), key=lambda x:x[1], reverse=True)
    
    if len(arr) == 1: #4개 같은 경우
        return 1111 * arr[0][0]
    if arr[0][1] == 3: #3개 같은 경우
        return (10 * arr[0][0] + arr[1][0]) ** 2
    if arr[0][1] == 2 and arr[1][1] == 2: #2개 같은 경우
        return (arr[0][0] + arr[1][0]) * abs(arr[0][0] - arr[1][0])
    if arr[0][1] == 2 and arr[1][1] == 1: #2 : 1 : 1 경우
        return arr[1][0] * arr[2][0]
    
    arr.sort(key=lambda x: x[0])
    return arr[0][0]
    
''' case1
def solution(a, b, c, d):
    arr = [a, b, c, d]
    set_arr = list({a, b, c, d})  #set 중복 제거

    if len(set_arr) == 1: #4개 같은 경우
        return 1111 * a
    if len(set_arr) == 2: # 중복 2개, 단 2:2 인지 3:1 인지 확인해야 함
        if arr.count(set_arr[0]) == 3: # 3:1경우
            return (10 * set_arr[0] + set_arr[1]) ** 2
        elif arr.count(set_arr[1]) == 3: # 3:1경우
            return (10 * set_arr[1] + set_arr[0]) ** 2   
        elif arr.count(set_arr[0]) == 2: # 2:경우 #(p + q) × |p - q|
            return (set_arr[0] + set_arr[1]) * abs(set_arr[0] - set_arr[1])
    if len(set_arr) == 3: #2:1:1 #q × r
        if arr.count(set_arr[0]) == 2:
            return set_arr[1] * set_arr[2]
        elif arr.count(set_arr[1]) == 2:
            return set_arr[0] * set_arr[2]
        else:
            return set_arr[0] * set_arr[1]
    return min(arr) 
'''
