#https://school.programmers.co.kr/learn/courses/30/lessons/181921
#배열 만들기 2

def solution(l, r):
    answer = []
    
    # for i in range(5, r+1, 5):
    for i in range(l, r+1):
        cnt5 = str(i).count('5')
        cnt0 = str(i).count('0')
        
        if len(str(i)) == cnt5 + cnt0:
            answer.append(i)
            
    if len(answer) == 0:
        return [-1]
    else:
        return answer
