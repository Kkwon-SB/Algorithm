#https://school.programmers.co.kr/learn/courses/30/lessons/120863
#다항식 더하기

def separate_polynomial(polynomial):
    polynomial = polynomial.split()
    x_num, num = 0, 0

    for i in range(0, len(polynomial), 2):
        if 'x' in polynomial[i]:
            if len(polynomial[i]) > 1:
                x_num += int(polynomial[i][:-1])
            else:
                x_num += 1
        else:
            num += int(polynomial[i])

    return x_num, num

def make_polynomial(x_num, num):
    answer = ''

    if abs(x_num) == 1:
        answer = 'x' if x_num > 0 else '-x'
    elif abs(x_num) > 1:
        answer = str(x_num) + 'x' if x_num > 1 else '-' + str(x_num) + 'x'

    if abs(num) > 0 and answer:
        answer += ' + ' + str(num) if num > 0 else ' - ' + str(num)
    elif abs(num) > 0:
        answer += str(num)

    return answer


def solution(polynomial):
    x_num, num = separate_polynomial(polynomial)
    return make_polynomial(x_num, num)

# def solution(polynomial):
#     polynomial = polynomial.split()    
#     answer = ''
#     x_num, num = 0, 0
    
#     #seperate
#     for i in range(0, len(polynomial), 2):
#         if 'x' in polynomial[i]:
#             if len(polynomial[i]) > 1:
#                 x_num += int(polynomial[i][:-1])
#             else:
#                 x_num += 1
#         else:
#             num += int(polynomial[i])
    
#     #making
#     if abs(x_num) == 1:
#         answer = 'x' if x_num > 0 else '-x'
#     elif abs(x_num) > 1:
#         answer = str(x_num) + 'x' if x_num > 1 else '-' + str(x_num) + 'x'
            
#     if abs(num) > 0 and answer:
#         answer += ' + ' + str(num) if num > 0 else ' - ' + str(num)
#     elif abs(num) > 0:
#         answer += str(num)
        
#     return answer
