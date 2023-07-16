#https://school.programmers.co.kr/learn/courses/30/lessons/120850
#문자열 정렬하기 (1)

def solution(my_string):
    answer = [int(i) for i in my_string if not i.isalpha()]
    answer.sort()
    return answer

#return sorted(map(int, (list(re.sub('[^0-9]', '', my_string)))))

#return sorted(map(int, filter(lambda s: s.isdigit(), my_string)))
