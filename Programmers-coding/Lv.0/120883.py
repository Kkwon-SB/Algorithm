#https://school.programmers.co.kr/learn/courses/30/lessons/120883
#로그인 성공?

def solution(id_pw, db):
    check = 'fail'
    
    for info in db:
        if info[0] == id_pw[0]:
            check = 'wrong pw'
            if info[1] == id_pw[1]:
                return 'login'
            
    return check
