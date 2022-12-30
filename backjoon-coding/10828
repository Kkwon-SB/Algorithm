#https://www.acmicpc.net/problem/10828
#스택


"""
파이썬은 따로 stack 구조를 제공하지 않는다.
기본 클래스 list를 이용하여 stack을 표현할 수 있다.

이때, input() 함수를 사용할 경우, 시간초과 에러가 뜨므로 시간단축을 위해 sys.stdin.readline()을 사용한다.
입출력 속도 비교 : sys.stdin.readline > raw_input() > input()
"""
import sys
n = int(sys.stdin.readline()) #input() 시간 초과 문제
num_list = []

for _ in range(n):
  word =  sys.stdin.readline().split()
  order = word[0]
  if order == 'push':
    num_list.append(word[1])
    

  elif order == 'pop':
    if len(num_list) == 0:
      print(-1)
    else:
      print(num_list.pop())
    

  elif order == 'size':
    print(len(num_list))

  elif order == 'empty':
    if len(num_list) == 0:
      print(1)
    else:
      print(0)

  elif order == 'top':
    if len(num_list) == 0:
      print(-1)
    else:
      print(num_list[-1])
