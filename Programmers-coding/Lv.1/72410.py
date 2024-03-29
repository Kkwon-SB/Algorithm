# https://school.programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    #1단계
    # new_id = new_id.lower()
    #1 & 2단계
    new_id = re.sub('[^a-zA-Z0-9\-\_\.]', '', new_id.lower())  
        # '\'붙여주는 이유는 정규표현식에서 기호는 기호 자체로 받아들여지지 않기 때문에
    #3단계
    new_id = re.sub('\.\.+', '.', new_id)
    #4단계
    new_id = re.sub('^\.|\.$', '', new_id)  #^맨 앞, $맨뒤
    #5단계
    if new_id == '':
        new_id = 'a'
    #6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = re.sub('\.$', '', new_id)
    #7단계
    if len(new_id) < 3:
        while len(new_id) != 3:
            new_id = new_id + new_id[-1]


    return (new_id)
    
    '''
    처음 시도) re 모듈을 사용하여 접근해야한다고 생각했다.
    과정) re모듈을 오랜만에 사용해서 딜레이 되는 시간이 많았다. 문제 차제는 어려운 문제는 아니었다고 생각한다.
    '''
    
    
#https://school.programmers.co.kr/learn/courses/30/lessons/72410
