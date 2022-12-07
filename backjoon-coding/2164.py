import sys
from collections import deque
N = int(sys.stdin.readline()) #sys.stdin.readline()은 시간초과 문제를 해결하기 위해 쓰여졌다
    #int를 함께 사용한 것은, 기본적으로 문자열 형태str 로 저장되기 때문, 
    #게다가 개행문자도 함께 포함되기 때문

queue = deque() 
for i in range(N):
    queue.append(i + 1) 
    
while len(queue) > 1: 
    queue.popleft() #일반 pop을 하면 가장 오른쪽에 있는, 마지막인덱스가 삭제되기 때문
    queue.append(queue.popleft()) #첫번째 인덱스를 마지막인덱스로 다시 준다. 
    
print(queue.pop())