#https://school.programmers.co.kr/learn/courses/30/lessons/76501
#음양 더하기

def solution(absolutes, signs):
    answer = 0
    
    for ab, si in zip(absolutes, signs):
        if si == True:
            answer += ab
        else:
            answer -= ab
            
    return answer
