#https://school.programmers.co.kr/learn/courses/30/lessons/120847
#최댓값 만들기 (1)

def solution(numbers):
    numbers.sort(reverse=True)
    return numbers[0] * numbers[1]
