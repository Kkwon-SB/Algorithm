#https://school.programmers.co.kr/learn/courses/30/lessons/181932

def solution(code):
    ret = ''
    mode = 0
    
    for idx in range(len(code)):
        if code[idx] == '1':
            mode = (mode+1) % 2
            continue
        
        if mode == 0 and idx % 2 == 0:
            ret += code[idx]
            
        elif mode == 1 and idx % 2 == 1:
            ret += code[idx]
        
    
    if len(ret) == 0:
        return "EMPTY"
    else:
        return ret
