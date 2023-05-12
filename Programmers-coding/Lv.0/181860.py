#https://school.programmers.co.kr/learn/courses/30/lessons/181860
#빈 배열에 추가, 삭제하기

def solution(arr, flag):
    answer = []
    
    for i in range(len(flag)):
        if flag[i] == True:
            answer += [arr[i]] * (arr[i] * 2)
        elif flag[i] == False:
            answer = answer[:-arr[i]]
    
    return answer
