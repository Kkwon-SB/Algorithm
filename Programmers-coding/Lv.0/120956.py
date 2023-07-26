#https://school.programmers.co.kr/learn/courses/30/lessons/120956
#옹알이 (1)

def solution(babbling):
    temp = ["aya", "ye", "woo", "ma"]
    
    for i in range(0, len(babbling)):
        for j in temp:
            if j in babbling[i]:
                babbling[i] = babbling[i].replace(j, ' ') 
                #replace 사용 시, 띄어 쓰기를 해서 구별하지 않으면 전 후에 있는 문자가 합쳐져 원래는 허용되지 않아야 하는 경우가 허용될 수 있기 때문 ex) woyeo
    
    return len([i for i in babbling if len(i.strip()) == 0 ])


'''
import re

def solution(babbling):
    regex = re.compile('^(aya|ye|woo|ma)+$')
    cnt=0
    for e in babbling:
        if regex.match(e):
            cnt+=1
    return cnt
'''
