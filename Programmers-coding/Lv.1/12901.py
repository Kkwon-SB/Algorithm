#https://school.programmers.co.kr/learn/courses/30/lessons/12901
#2016년

import datetime
def solution(a, b):
    day = datetime.date(2016, a, b).weekday()
    
    if day == 0:
        return "MON"
    elif day == 1:
        return "TUE"
    elif day == 2:
        return "WED"
    elif day == 3:
        return "THU"
    elif day == 4:
        return "FRI"
    elif day == 5:
        return "SAT"
    elif day == 6:
        return "SUN"
    
