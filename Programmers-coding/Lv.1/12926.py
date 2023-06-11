#https://school.programmers.co.kr/learn/courses/30/lessons/12926
#시저 암호

'''
s문자열을 리스트로 변환 -> 공백 유지x
문자열 for순회하면서 새로운 answer만들기
각 원소를 아스키코드로 변환 후 n만큼 추가 
대소문자 구분
z다음에는 a, Z 다음에 A 일것
a = 97 ~ 122 A = 65 ~ 90 
n은 25이하라 대문자에서 소문자로 안넘어감
'''
def solution(s, n):
    answer = ''
    
    for i in s:
        if i == ' ':  #공백
            answer += ' '
            continue
            
        asc = ord(i)
        if asc <= 90: #대문자
            t = 0
        else:         #소문자
            t = 1

        asc += n
            
        if (t == 0 and asc > 90) or (t == 1 and asc > 122):
            asc -= 26
            answer += chr(asc)
        else:
            answer += chr(asc)
            
    return answer
