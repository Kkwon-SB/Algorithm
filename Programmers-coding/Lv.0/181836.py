#https://school.programmers.co.kr/learn/courses/30/lessons/181836
#그림 확대

def solution(picture, k):
    answer = ''
    std = len(picture[0])
    _picture = ''.join(picture)
    
    for i in _picture:
        answer += i * k
        
    result = []
    for i in range(std*k, len(answer)+1, std*k):
        for _ in range(k):
            result.append(answer[i-(std*k):i])
    

    return result
