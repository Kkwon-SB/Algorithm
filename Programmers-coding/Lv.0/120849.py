#https://school.programmers.co.kr/learn/courses/30/lessons/120849
#모음 제거

def solution(my_string):
    
    temp = ['a','e','i','o','u']
    my_string = list(my_string)
    
    for i in range(len(my_string)-1, -1, -1):
        if my_string[i] in temp:
            my_string.pop(i)
            
    return ''.join(my_string)
            
    #return "".join([i for i in my_string if not(i in "aeiou")])
    #my_string.replace(vowel, '')
