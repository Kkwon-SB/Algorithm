#https://school.programmers.co.kr/learn/courses/30/lessons/120839
#가위 바위 보

def solution(rsp):
    
    morse = {'2':'0','0':'5','5':'2'}
    
    return ''.join(morse[i] for i in rsp)
