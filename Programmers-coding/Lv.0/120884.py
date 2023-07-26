#https://school.programmers.co.kr/learn/courses/30/lessons/120884
#치킨 쿠폰

def solution(chicken):
    coupon = 0
    answer = 0
    
    while chicken:
        chicken += coupon
        chicken, coupon = divmod(chicken, 10)
        answer += chicken
        
    return answer
