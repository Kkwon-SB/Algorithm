#https://school.programmers.co.kr/learn/courses/30/lessons/120837
#개미 군단

def solution(hp):
    cnt = 0
    
    if hp >= 5:
        a, hp = divmod(hp, 5)
        cnt += a
        
    if hp >= 3:
        b, hp = divmod(hp, 3)
        cnt += b

    cnt += hp
        
    return cnt

    #return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)
