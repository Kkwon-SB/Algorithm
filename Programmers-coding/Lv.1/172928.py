#https://school.programmers.co.kr/learn/courses/30/lessons/172928
#공원 산책

def solution(park, routes):
    answer = []
    
    #시작 위치 파악
    now = []
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                now = [i,j]
    
    #검증 과정
    h_size = len(park) -1
    w_size = len(park[0]) -1
    
    for route in routes:
        foward, distance = route.split()
        distance = int(distance)
        check = True
        
        if foward == 'E' and now[1]+distance <= w_size:#범위 내 확인
            for i in range(1, distance+1): #장애물 확인
                if park[now[0]][now[1]+i] == 'X':
                    check = False
                    break      
            if check == True:
                now[1] += distance
            
        elif foward == 'W' and now[1]-distance >= 0:#범위 내 확인
            for i in range(1, distance+1): #장애물 확인
                if park[now[0]][now[1]-i] == 'X':
                    check = False
                    break      
            if check == True:
                now[1] -= distance
                
        elif foward == 'S' and now[0]+distance <= h_size:#범위 내 확인
            for i in range(1, distance+1): #장애물 확인
                if park[now[0]+i][now[1]] == 'X':
                    check = False
                    break      
            if check == True:
                now[0] += distance
                
        elif foward == 'N' and now[0]-distance >= 0:#범위 내 확인
            for i in range(1, distance+1): #장애물 확인
                if park[now[0]-i][now[1]] == 'X':
                    check = False
                    break      
            if check == True:
                now[0] -= distance
        check = True
        
    return now
