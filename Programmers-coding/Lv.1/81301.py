#https://school.programmers.co.kr/learn/courses/30/lessons/81301
#숫자 문자열과 영단어


# eng_num = ['zero','one','two','three','four','five','six','seven','eight','nine']
# def solution(s):
#     answer = s
#     for i in range(len(eng_num)):
#         answer = answer.replace(eng_num[i], str(i))
#     return int(answer)

def solution(s):

    if 'one' in s:
        s = s.replace('one', '1') #자체 저장이 안됨
    if 'two' in s:
        s = s.replace('two', '2')
    if 'three' in s:
        s = s.replace('three', '3')
    if 'four' in s:
        s = s.replace('four', '4')
    if 'five' in s:
        s = s.replace('five', '5')
    if 'six' in s:
        s = s.replace('six', '6')
    if 'seven' in s:
        s = s.replace('seven', '7')
    if 'eight' in s:
        s = s.replace('eight', '8')
    if 'nine' in s:
        s = s.replace('nine', '9')
    if 'zero' in s:
        s = s.replace('zero', '0')

    return int(s)
