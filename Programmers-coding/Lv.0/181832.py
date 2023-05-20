#https://school.programmers.co.kr/learn/courses/30/lessons/181832
#정수를 나선형으로 배치하기

def solution(n):
    maps = [[0] * n for _ in range(n)]
    i = 1
    x, y = 0, 0
    
    while i <= (n * n):
        for p in range(n): #왼쪽 -> 오른쪽
            if maps[x][p] == 0:
                maps[x][p] = i
                i += 1
                y = p

        for p in range(n): #위 -> 아래
            if maps[p][y] == 0:
                maps[p][y] = i
                i += 1
                x = p 
                
        for p in range(x, -1, -1): #오른쪽 -> 왼쪽
            if maps[x][p] == 0:
                maps[x][p] = i
                i += 1
                y = p
            
        for p in range(x, -1, -1): #아래 -> 위
            if maps[p][y] == 0:
                maps[p][y] = i
                i += 1
                x = p
    
    return maps
