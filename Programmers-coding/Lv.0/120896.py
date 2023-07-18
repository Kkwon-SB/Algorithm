#https://school.programmers.co.kr/learn/courses/30/lessons/120896
#한 번만 등장한 문자

def solution(s):
    
    return "".join(sorted([ i for i in set(s) if s.count(i) == 1]))

'''
    dict_word = {}
    answer = ''
    for i in s:
        if i not in dict_word:
            dict_word[i] = 1
        else:
            dict_word[i] += 1
    
    answer = [i for i, j in dict_word.items() if j == 1]
    answer.sort()
    
    return ''.join(answer)

'''
