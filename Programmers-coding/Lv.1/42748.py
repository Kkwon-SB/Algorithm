#https://school.programmers.co.kr/learn/courses/30/lessons/42748
#K번째수

def solution(array, commands):
    answer = []
    
    for a, b, c in commands:
        answer.append(sorted(array[a-1:b])[c-1])
        
    return answer

        # aa = array[a-1:b]
        # aa.sort()
        # answer.append(aa[c-1])
