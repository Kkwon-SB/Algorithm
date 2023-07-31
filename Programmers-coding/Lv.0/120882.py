#https://school.programmers.co.kr/learn/courses/30/lessons/120882
#등수 매기기

def solution(score):
    rank = 1
    score = [(i+j)/2 for i,j in score ]
    score2 = sorted(set(score), reverse=True)
    total = {}
    
    for i in score2:
        cnt = score.count(i)
        
        if i in total:
            continue
        elif cnt == 1:
            total[i] = rank
            rank += cnt
        else:
            total[i] = rank
            rank += cnt
            
    return [total[i] for i in score]
