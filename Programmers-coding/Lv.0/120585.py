#https://school.programmers.co.kr/learn/courses/30/lessons/120585
#머쓱이보다 키 큰 사람

def solution(array, height):
    array.sort(reverse=True)
    cnt = 0


    for i in array:
        if i > height:
            cnt += 1
        else:
            return cnt
    
    return cnt

    #return sum(1 for i in array if i > height)
