#스택

import sys
n = int(sys.stdin.readline())
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