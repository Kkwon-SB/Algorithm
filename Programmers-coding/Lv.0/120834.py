#https://school.programmers.co.kr/learn/courses/30/lessons/120834
#외계행성의 나이

def solution(age):
    temp = ['a','b','c','d','e','f','g','h','i','j']
    answer = ''
    
    for i in str(age):
        answer += temp[int(i)]
    
    return answer

    
'''
    temp = {'0':'a','1':'b','2':'c','3':'d','4':'e','5':'f','6':'g','7':'h','8':'i','9':'j'}
    
    return ''.join(temp[i] for i in str(age))
'''
