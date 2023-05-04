#https://school.programmers.co.kr/learn/courses/30/lessons/181904
#세로 읽기

def solution(my_string, m, c):
    result = ''
    for i in range(0, len(my_string), m):
        # my_arr.append(my_string[i:i+m])
        result += my_string[i:i+m][c-1]

    return result
