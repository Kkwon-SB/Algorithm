"""
one = [1, 2, 3, 4, 5]
two = [2, 1, 2, 3, 2, 4, 2, 5]
three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
students = [one, two, three]
max = 0

def solution(answers):
    result = []
    for j in range(3):
        cnt = 0
        for i in range(len(answers)):
            if answers[i] == students[j][i]:
                cnt += 1  
        if j == 0:
            max = cnt
            
            result.append(j+1)
        elif max > cnt:
            pass
        elif max < cnt:
            max = cnt
            result = []
            result.append(j+1)
        else:
            result.append(j+1)  
    return result

    """

def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers): #enumerate -> for문 기능 + 인덱스 순서 값도 같이 받는다 
        if answer == one[idx%len(one)]:
            score[0] += 1
        if answer == two[idx%len(two)]:
            score[1] += 1
        if answer == three[idx%len(three)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result