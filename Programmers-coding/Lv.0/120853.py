#https://school.programmers.co.kr/learn/courses/30/lessons/120853
#컨트롤 제트

def solution(s):
    s = s.split()
    answer = 0
    check = False
    
    for i in range(len(s)-1, -1, -1):
        if check == True:
            check = False
            continue
        
        if s[i] == "Z":
            check = True
            continue
            
        answer += int(s[i])
    
    return answer
        
    
'''
def solution(s):
    
    answer = []
    
    for a in s.split():
    
        if a != 'Z':
            answer.append(int(a))
        else:
            answer.pop()

    return sum(answer)
'''
