#https://school.programmers.co.kr/learn/courses/30/lessons/181838
#날짜 비교하기

def solution(date1, date2):
    date1 = ''.join(str(i) for i in date1)
    date2 = ''.join(str(i) for i in date2)

    return 1 if int(date1) < int(date2) else 0
'''
처음 시도했던 방법 -  8 9 10 11번? 실패 나왔다.)
return 1 if date1 < date2 else 0

문자열 비교 시 사전식 순서에 따라, 각 자리가 의미하는 아스키코드 값을 기준으로 비교하게 되는데,
문자열 0 ~ 9까지 오름차순으로 아스키코드 값을 가지기 때문에 '처음 시도했던 방법'도 같은 결과 값이 나올 것이라 생각했다. 계속된 실패로 혹시나 하는 마음에 정수형으로 바꾼 뒤로는 pass 결과가 나왔다.  

아마 각 자리 값을 0으로 채워주는 것이 아닌 값 그대로 준것 같다. 
ex) 06 x  ->  6  
위와 같은 경우  a = [2021, 12, 28], b =  [2021, 6, 28] 문자열 비교 시 월 단위의 1 과 6이 비교 되기 때문에 a가 더 작은 값을 가진다.
'''
