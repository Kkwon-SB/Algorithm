#https://school.programmers.co.kr/learn/courses/30/lessons/181897
#리스트 자르기

def solution(n, slicer, num_list):
    answer = []
    #  a, b, c = slicer
    if n == 1:
        return num_list[:slicer[1]+1]
    if n == 2:
        return num_list[slicer[0]:]
    if n == 3:
        return num_list[slicer[0]:slicer[1]+1]
    if n == 4:
        target = num_list[slicer[0]:slicer[1]+1]
        
        for i in range(0, len(target), 2):
            answer.append(target[i])
            
        return answer
        
        #return num_list[a:b+1:c]
    
