#https://school.programmers.co.kr/learn/courses/30/lessons/42576
#완주하지 못한 선수

def solution(participant, completion):

    answer = ''
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if(participant[i] != completion[i]):
            return participant[i]

    return participant[-1]
   
