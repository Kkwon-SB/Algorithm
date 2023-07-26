#https://school.programmers.co.kr/learn/courses/30/lessons/120864
#숨어있는 숫자의 덧셈 (2)

import re

def solution(my_string):

    # return sum([int(i) for i in re.findall(r'[0-9]+', my_string)])

    answer = re.sub('[^0-9]', ' ', my_string).split()
    return sum([int(i) for i in answer])

'''
def solution(my_string):

    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i, ' ')
    
    my_string = my_string.split()
    
    return sum([int(i) for i in my_string])
'''
