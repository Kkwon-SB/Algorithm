#https://school.programmers.co.kr/learn/courses/30/lessons/181885
#할 일 목록

def solution(todo_list, finished):
    answer = []
    
    for todo, result in zip(todo_list, finished):
        if result == False:
            answer.append(todo)
    
    return answer
