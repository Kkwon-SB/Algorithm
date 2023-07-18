#https://school.programmers.co.kr/learn/courses/30/lessons/120894
#영어가 싫어요

def solution(numbers):
    numbers = numbers.replace('zero', '0').replace('one', '1').replace('two', '2').replace('three', '3').replace('four', '4').replace('five', '5').replace('six', '6').replace('seven', '7').replace('eight', '8').replace('nine', '9')

    return int(numbers)

'''
def solution(numbers):
    r = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',\
         'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for k in r.keys():
        numbers = numbers.replace(k, r[k])
'''
