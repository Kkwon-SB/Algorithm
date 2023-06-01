#https://school.programmers.co.kr/learn/courses/30/lessons/178871
#달리기 경주

def solution(players, callings):
    
    d_p = {name : idx for idx, name in enumerate(players)}
    
    for i in callings:
        target, now = d_p[i] - 1, d_p[i]
        players[target], players[now] = players[now] , players[target]
        d_p[players[target]], d_p[players[now]] = d_p[players[target]] -1, d_p[players[now]] +1
        
        
    return players


