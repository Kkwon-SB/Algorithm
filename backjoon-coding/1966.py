#https://www.acmicpc.net/problem/1966
#프린터 큐

from collections import deque

a = int(input())

for _ in range(a):
    priorities = list(map(int, input().split(' ')))
    documents = list(map(int, input().split(' ')))

    ori_num = documents[priorities[1]]

    documents[priorities[1]] += 0.5
    c = deque(documents)
    cnt = 0

    while True: #기준 값 보다 큰 수 제거 & 카운트
        if max(c) == ori_num+0.5:
            break
        elif c[0] != max(c):
            c.rotate(-1)
        elif c[0] == max(c):
            c.popleft()
            cnt += 1
    while True:
        if c[0] == ori_num+0.5:
            cnt+=1
            break
        elif c[0] < ori_num:
            c.rotate(-1)
        else: #같은 경우
            c.popleft()
            cnt += 1

    print(cnt)
