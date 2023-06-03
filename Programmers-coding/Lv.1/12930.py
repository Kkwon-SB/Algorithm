#https://school.programmers.co.kr/learn/courses/30/lessons/12930
#이상한 문자 만들기

def solution(s):
    result = []
    words = s.split(" ")
    for word in words:
        new_word = ""
        for i in range(len(word)):
            if i % 2 == 0:
                new_word += word[i].upper()
            else:
                new_word += word[i].lower()
        result.append(new_word)
    return " ".join(result)


# def solution(s):
#     ori = s
#     ori_s = s.split(' ')
#     answer = s.split()

#     for i in range(len(answer)):
#         temp = answer[i]
#         temp = list(temp.lower())

#         for j in range(0,len(temp),2):
#             temp[j] = temp[j].upper() 
        
#         answer[i] = temp
        
#     answer = [''.join(word) for word in answer]
    
#     for i in range(len(ori_s)):
#         if ori_s[i]:
#             ori_s[i] = answer[0]
#             del answer[0]
#     return ' '.join(ori_s)
