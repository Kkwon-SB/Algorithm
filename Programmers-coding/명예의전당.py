'''
Time 30m

사전 계획

1. for문 순환
2. 리스트 변수로 sort정렬, 맨 앞에 작은 값이 오도록
3. 값 비교 후 크다면 맨 앞 인덱스(작은 값) 변경
4. answer 에 값 append

'''

#전
def solution(k, score):
    answer = []
    honor_list = []
    
    for i in score:

        honor_list.sort()
        if len(honor_list) < k:
            honor_list.append(i)
            answer.append(honor_list[0])          
        elif honor_list[0] < i:
            honor_list[0] = i
            honor_list.sort()
            answer.append(honor_list[0])
        else:
            answer.append(honor_list[0])

    return answer

 '''
 테스트는 통과 했지만 , 제점에서 80% 오답이 나왔다.
 주어진 경우의 수가 적어 확인이 어려움...
 좀 더 효율적인 코드로 실행 -> 성공

먼저 작성한 코드가 더 복잡한 것은 맞지만 문제에서 왜 틀렸는지는 잘 모르겠다.
 '''
  
#후
def solution(k, score):
    honor, answer = [], []
    
    for i in score:
        honor.append(i)

        if len(honor) > k:
            honor.remove(min(honor))
            answer.append(min(honor))
        else:
            answer.append(min(honor))
    return answer
