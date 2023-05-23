#https://school.programmers.co.kr/learn/courses/30/lessons/176963
#추억 점수

def solution(name, yearning, photo):
     
    na_ye = {string : num for string, num in zip(name, yearning)} #dict(zip(name,yearning))
    total = 0
    result = []
    
    for pho in photo:
        for person in pho:
            if person in name:
                total += na_ye[person]
        result.append(total)
        total = 0
    
    return result
