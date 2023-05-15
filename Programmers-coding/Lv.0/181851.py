#https://school.programmers.co.kr/learn/courses/30/lessons/181851
#전국 대회 선발 고사

def solution(rank, attendance):
    answer = []
    temp = rank[:]
    temp.sort()

    for i in range(len(rank)):
        if attendance[rank.index(temp[i])] == True:
            answer.append(rank.index(temp[i]))        
            if len(answer) == 3:
                break
    
    return answer[0] * 10000 + (100 * answer[1]) + answer[2]
    
