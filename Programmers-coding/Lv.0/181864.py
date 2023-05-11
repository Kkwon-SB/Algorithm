#https://school.programmers.co.kr/learn/courses/30/lessons/181864
#문자열 바꿔서 찾기

def solution(myString, pat):
    result = ''.join(['B' if i == 'A' else 'A' for i in myString])
    
    return 1 if pat in result else 0 


'''
def solution(myString, pat):
    #[i if i%2==0 else 'odd' for i in range(5)]
    a = ['B' if i == 'A' else 'A' for i in myString ]
    result = ''.join(map(str, a)
                     
    return result
'''
