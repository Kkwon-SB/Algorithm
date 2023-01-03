#https://www.acmicpc.net/problem/1546
#평균

subjects = int(input())

scores = list(map(int, input().split()))

# max_num = max(scores) 반복문이 길어질 경우 따로 값을 저장해서 사용하는 것이 효율적인 측면에서 좋을 것 같다.

for i in range(len(scores)):
    scores[i] = scores[i] / max(scores) * 100

print(sum(scores)/subjects)

'''
에러 종류 - TypeError
에러 메시지 - TypeError: ‘list’ object is not callable
발생 이유 - 함수와 변수명이 중복되었을 때 발생
python에서 쓰이는 함수를 변수명으로 선언한 뒤, 밑에서 그 함수를 호출하려고 하면 해당 에러가 발생한다.
해결 방법 - 에러가 난 함수와 같은 이름의 변수가 있는지 확인
'''


'''
#더 짧은 코드로 구현한 방법(외부 답 참고)
subjects = int(input())

scores = list(map(int, input().split()))

mymax = max(scores)
mysum = sum(scores)

print(mysum * 100 / mymax / subjects)
'''
